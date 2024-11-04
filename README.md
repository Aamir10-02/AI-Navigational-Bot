# AI Chatbot with Flask Web Interface

Welcome to the AI Chatbot project! This repository contains a sophisticated AI-powered chatbot implemented using PyTorch, Flask, and various NLP libraries. The chatbot is capable of both text and voice interactions, making it versatile for various applications.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Introduction

This project demonstrates the integration of natural language processing (NLP) with a neural network model to create a chatbot capable of understanding and responding to user queries. It leverages Flask for the web interface and PyTorch for building and training the neural network.

## Features

- **Text-based interaction**: Users can interact with the chatbot using text input.
- **Voice-based interaction**: Users can interact with the chatbot using voice input.
- **Neural Network**: Uses PyTorch to train a neural network model for intent classification.
- **Natural Language Processing**: Utilizes NLTK for tokenizing and stemming user inputs.

## Architecture

1. **Frontend**: HTML, CSS (contained in the `templates` and `static` directories).
2. **Backend**: Flask web framework for handling requests and responses.
3. **AI Model**: PyTorch-based neural network for classifying user intents.
4. **NLP**: NLTK for tokenizing and processing text.

## Setup and Installation

### Prerequisites

- Python 3.6+
- Virtualenv (recommended)

### Installation Steps

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/ai-chatbot.git
    cd ai-chatbot
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv\Scripts\activate 
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK data**
    ```python
    import nltk
    nltk.download('punkt')
    ```

## Usage

### Running the Web Application

1. **Start the Flask app**
    ```bash
    python application.py
    ```

2. **Access the application**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

### Interacting with the Chatbot

- **Text Interaction**: Use the provided text box on the homepage.
- **Voice Interaction**: Upload an audio file on the designated page for voice input.

## Project Structure

```plaintext
my-flask-app/
├── application.py          # Main Flask application
├── chat.py                 # Chatbot logic
├── requirements.txt        # List of dependencies
├── .ebextensions/          # Elastic Beanstalk configuration
│   └── flask.config
├── templates/              # HTML templates
│   ├── base.html
│   ├── about.html
│   └── contact.html
└── static/                 # Static files 
```

## Model Training

The model is trained using intents data provided in intents.json. Follow the steps in chat.py to preprocess the data and train the model. The trained model is saved as data.pth.


## Acknowledgements
NLTK: Natural Language Toolkit for text processing.
PyTorch: Deep learning framework for building and training the neural network.
Flask: Web framework for creating the web interface.
SpeechRecognition: Library for converting speech to text.
pyttsx3: Text-to-speech conversion library.

requirements.txt file should include following packages 

```plaintext
Flask
torch
nltk
numpy
pyttsx3
SpeechRecognition
```
Installing the Packages:


```plaintext
pip install flask
```
```plaintext
pip install nltk
```
```plaintext
pip install numpy
```
If required then download lower version of numpy.
```plaintext
pip install numpy <2
```

```plaintext
pip install pyttsx3
```
```plaintext
pip install SpeechRecognition
```
## License
This project is licensed under the
[MIT](https://github.com/Aamir10-02/AI-Navigational-Bot/blob/main/LICENSE) License - see the LICENSE file for details. 
This project is a great demonstration of combining deep learning with web development to create a functional and interactive application. I hope you enjoy using it as much as I enjoyed building it!
