from flask import Flask, render_template, request, jsonify, url_for
from chat import get_response

app = Flask(__name__)

# Define routes for each HTML page
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
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)


