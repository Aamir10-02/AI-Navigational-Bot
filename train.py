import json
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from model import NeuralNet
from nltk_utils import tokenize, stem, bag_of_words

# Load intent data from JSON
with open('intents.json', 'r') as file:
    intent_data = json.load(file)

# Initialize lists for storing words and tags
word_list = []
tag_list = []
data_points = []

# Process each intent and pattern
for intent in intent_data['intents']:
    category = intent['tag']
    tag_list.append(category)
    for pattern in intent['patterns']:
        tokens = tokenize(pattern)
        word_list.extend(tokens)
        data_points.append((tokens, category))

# Remove punctuation and stem words
ignore_chars = ['?', '!', '.', ',']
word_list = [stem(word) for word in word_list if word not in ignore_chars]
word_list = sorted(set(word_list))
tag_list = sorted(set(tag_list))

# Prepare training data
features = []
labels = []
for (sentence, category) in data_points:
    bag = bag_of_words(sentence, word_list)
    features.append(bag)
    label = tag_list.index(category)
    labels.append(label)

features = np.array(features)
labels = np.array(labels)

# Define custom dataset class
class DialogueDataset(Dataset):
    def __init__(self):
        self.num_samples = len(features)
        self.inputs = features
        self.targets = labels

    def __getitem__(self, index):
        return self.inputs[index], self.targets[index]

    def __len__(self):
        return self.num_samples

# Hyperparameters
batch_size = 12
hidden_dim = 12
num_classes = len(tag_list)
input_dim = len(features[0])
learning_rate = 0.001
epochs = 1000

# Create dataset and data loader
dataset = DialogueDataset()
data_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

# Set device for training
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_dim, hidden_dim, num_classes).to(device)

# Define loss function and optimizer
loss_function = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(epochs):
    for (inputs, targets) in data_loader:
        inputs = inputs.to(device)
        targets = targets.to(dtype=torch.long).to(device)

        # Forward pass
        outputs = model(inputs)
        loss = loss_function(outputs, targets)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    if (epoch + 1) % 100 == 0:
        print(f'Epoch {epoch+1}/{epochs}, Loss={loss.item():.4f}')

print(f'Final loss: Loss={loss.item():.4f}')

# Save model and metadata
model_data = {
    "model_state": model.state_dict(),
    "input_dim": input_dim,
    "hidden_dim": hidden_dim,
    "num_classes": num_classes,
    "word_list": word_list,
    "tag_list": tag_list
}

file_path = "model_data.pth"
torch.save(model_data, file_path)

print(f'Training complete. Model saved to {file_path}')
