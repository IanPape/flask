# Put your app in here.
from flask import Flask

app = Flask(__name__)

# ... Define routes and application logic ...
@app.route('/welcome')
def welcome_msg():
    return '<h1> Welcome! </h1>'

@app.route('/welcome/home')
def welcome_home():
    return '<h1> Welcome Home! </h1>'

@app.route('/welcome/back')
def welcome_back():
    return '<h1> Welcome Back! </h1>'