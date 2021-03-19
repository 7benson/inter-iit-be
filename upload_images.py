# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:23:05 2021

@author: Dell
"""
import os
from flask import Flask, render_template,flash, request, redirect, url_for,send_from_directory,jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
def upload_image(request):
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
            return jsonify("File uploaded")
        else:
            return jsonify("Uploaded file is not an image")
    return jsonify("Wrong request method")



