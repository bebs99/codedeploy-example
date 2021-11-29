from flask import Flask, render_template, redirect, url_for, request# Route for handling the login page logic
app = Flask(__name__)@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')#within app.route add the html page we are doing changes to
@app.route('/')
# def is normally how we define a function in python
def home():
 return render_template('home.html')
