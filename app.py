# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:41:54 2021

@author: Dell
"""
from flask import Flask,request
from upload_images import upload_image
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/upload', methods=['POST'])
def upload():
   c = upload_image(request)
   return c

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run()