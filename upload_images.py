# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:23:05 2021

@author: Dell
"""
import os
from flask import Flask, render_template,flash, request, redirect, url_for,send_from_directory,jsonify
from werkzeug.utils import secure_filename
import pymysql


cwd = os.getcwd()
# mydb = pymysql.connect(host='localhost',
#     user='root',
#     passwd='',
#     db='inter_iit')
# cursor = mydb.cursor()

UPLOAD_FOLDER = 'static/uploaded_images'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def add_image_to_db(img_name,dbname,cl,path):
    sql = "INSERT INTO `images` (`org_image_name`,`db_image_name`,`class`,`image_loc`) \
                             VALUES ('%s','%s','%s','%s')" % (img_name,dbname,cl,path)
    #print(sql)
    cursor.execute(sql)
    mydb.commit()

    sql = "UPDATE `classes` SET `number_of_images` = `number_of_images` + 1 \
                WHERE `class` = '%s' " % (cl)
    #print(sql)
    cursor.execute(sql)
    mydb.commit()

def get_id(cl):
    sql = "SELECT `number_of_images` from `classes`\
                WHERE `class` = '%s' " % (cl)
    #print(sql)
    cursor.execute(sql)
    record = cursor.fetchone()
    if record == None:
        return -1
    return record[0]

def check_name(filename,cl):
    # sql = "SELECT `org_image_name` from `images`\
    #             WHERE `class` = '%s' AND `org_image_name` = '%s'" % (cl,filename)
    # #print(sql)
    # cursor.execute(sql)
    # record = cursor.fetchone()
    # if record == None:
    #     return -1
    return -1

# def upload_image(request):
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return jsonify("No file part")
#         if 'class' not in request.values:
#             return jsonify("No class defined")
#         file = request.files['file']
#         c = request.values['class']
#         if file.filename == '':
#             return jsonify("No selected file")
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             ret = check_name(filename,c)
#             if ret == -1 :
#                 path = os.path.join(UPLOAD_FOLDER, filename)
#                 file.save(path)
#                 dbname = str(c)+'_'+str(get_id(c)+1)
#                 path = os.path.join(cwd,path)
#                 add_image_to_db(filename,dbname,c,path)
#                 return jsonify("File uploaded")
#             else:
#                 return jsonify("Already an image with same name and class exists.Please re-check the image once or change the name of the image.")
#         else:
#             return jsonify("Uploaded file is not an image")
    
#     # cursor.close()
#     return jsonify("Wrong request method")

# sockets

def upload_image(request):
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify("No file part")
        if 'class' not in request.values:
            return jsonify("No class defined")
        files = request.files.getlist("file")
        # (files) = request.files
        print(files,"\n",files[0])
        cnt = 0
        c = request.values['class']
        for file in files:
            if file.filename == '':
                continue
            if file and allowed_file(file.filename):
                    path = os.path.join(UPLOAD_FOLDER, file.filename)
                    file.save(path)
                    # function
                    path = os.path.join(cwd,path)
                    cnt+=1
                # else:
                #     return jsonify("Already an image with same name and class exists.Please re-check the image once or change the name of the image.")
            else:
                continue
    
    return jsonify(f"{cnt} images uplaoded ") 
