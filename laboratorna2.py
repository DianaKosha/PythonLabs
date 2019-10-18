#the first option
from functools import wraps
from flask import escape

def my_escape_1(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return escape(func(*args, **kwargs))
    return wrapped

@app.route('/')
@my_escape_1
def index():
    return "<html></html>"

#second option
import cgi

def my_escape_2(func):
    def wrapped(*args, **kwargs):
        return cgi.escape(func(*args, **kwargs))
    return wrapped

@my_escape_2
def index():
    return "<html></html>"
print index()
