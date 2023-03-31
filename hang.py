from flask import Flask,render_template,redirect,request, session
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
  
@app.route('/game')
def game():
    warnings_counter = 3
    letter = request.form["letter"]
    if not re.match("^[a-zA-Z*]*$", letter):
        warnings_counter -=1
    
    
    