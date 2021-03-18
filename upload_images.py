# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:23:05 2021

@author: Dell
"""
import os
from flask import Flask, render_template,flash, request, redirect, url_for,send_from_directory,jsonify
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route('/upload', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify("No file part")
        file = request.files['file']
        if file.filename == '':
            return jsonify("No selected file")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            return  jsonify("File uploaded")
    return jsonify("Wrong request method")



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    #sess.init_app(app)
    app.run()