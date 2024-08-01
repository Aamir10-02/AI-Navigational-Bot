import random
import json
import torch
import pyttsx3
import speech_recognition as sr
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize


# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def recognize_speech(audio_file_path):
    """Convert speech to text using the speech recognition library"""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        print("Recognizing...")
        try:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Sorry, there was an error with the speech recognition service."

# Load model and data
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def get_response(msg):
    """Generate a response from the chatbot model"""
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    probs = torch.softmax(output, dim=1)
    confidence = probs[0][predicted.item()].item()

    matching_intent = None
    if confidence > 0.70:
        matching_intent = next((intent for intent in intents['intents'] if tag == intent["tag"]), None)

    if matching_intent:
        return random.choice(matching_intent['responses'])

    return "I do not understand..."