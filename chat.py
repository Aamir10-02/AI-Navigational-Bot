import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"  #load preprossed data
# data = torch.load(FILE) # information needed for the model
data = torch.load(FILE, weights_only=True)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)  #finds position of the biggest number in the row.

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    confidence = probs[0][predicted.item()].item()

    matching_intent = None

    if confidence > 0.70:

       matching_intent = next((intent for intent in intents['intents'] if tag == intent["tag"]), None)


    if matching_intent:
        return random.choice(matching_intent['responses'])


    return "I do not understand..."


if __name__ == "__main__":
    print("How can i help you")
    while True:
        
        sentence = input("You: ")
        if sentence == "over":
            break

        resp = get_response(sentence)
        print(resp)





    # probs = torch.softmax(output, dim=1)
    # prob = probs[0][predicted.item()]
    # if prob.item() > 0.80:
    #     for intent in intents['intents']:
    #         if tag == intent["tag"]:
    #             return random.choice(intent['responses'])
    
    # return "I do not understand..."