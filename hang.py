from flask import Flask,render_template,redirect,request, session
import hangman
import functions
import re
import string
import sys

app = Flask(__name__) 

@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
  