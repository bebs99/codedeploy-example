from flask import Flask, render_template, url_for, # Route for handling the login page logic

app = Flask(__name__)@app.route('/', methods=['GET', 'POST'])

def home():
    return render_template('home.html')

