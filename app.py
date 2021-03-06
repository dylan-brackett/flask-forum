'''
This is a simple, bootstrap based, flask "forum" platform
'''

from flask import Flask, render_template
from datetime import datetime
import re
from post import Post
from thread import Thread

__name__ = 'Forum'
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.context_processor
def inject_time():
    return {'cur_time': datetime.utcnow()}

""" @app.context_processor
def inject_nav():
    return {'navigation_bar': [
    ('/', 'index', 'Index'),
    ('/downloads/', 'downloads', 'Downloads'),
    ('/about/', 'about', 'About')
]} """
