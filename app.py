# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:41:54 2021

@author: Dell
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()