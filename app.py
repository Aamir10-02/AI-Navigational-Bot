from flask import Flask, render_template, request, jsonify, url_for
from chat import get_response, recognize_speech
import os

app = Flask(__name__)

# Define routes for HTML pages
@app.route('/')
def home():
    home_url = url_for('home', _external=True)
    return render_template('base.html', home_url=home_url)

@app.route('/about')
def about():
    about_url = url_for('about', _external=True)
    return render_template('about.html', about_url=about_url)

@app.route('/contact')
def contact():
    contact_url = url_for('contact', _external=True)
    return render_template('contact.html', contact_url=contact_url)

@app.route("/predict", methods=["POST"])
def predict():
    """Handle text input from the user"""
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

@app.route('/voice', methods=['POST'])
def voice():
    """Handle voice input from the user"""
    if 'audio' not in request.files:
        return jsonify({'answer': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    audio_file_path = os.path.join('tmp', audio_file.filename)
    audio_file.save(audio_file_path)

    text = recognize_speech(audio_file_path)
    os.remove(audio_file_path)  # Clean up the file after processing
    response = get_response(text)
    
    return jsonify({'answer': response})

if __name__ == "__main__":
    app.run(debug=True)
