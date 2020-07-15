#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, session
import json
from flask_socketio import SocketIO
from gensim.models import word2vec
import sys
import MeCab
import gensim
from flask_cors import CORS

from ImageNet import VGG16
import numpy as np
from waitress import serve

async_mode = None
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode = async_mode)
thread = None

vgg16 = VGG16()

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route("/", methods=['POST'])
def iDeea():
    if request.method == "POST":
        word = request.form['word']
        width = int(request.form['width'])
        height = int(request.form['height'])
        #print(word)
        words=word.split(',')
        image_array = [int(data) for i,data in enumerate(words) if i%4 != 3]
        print(image_array[:5])
        image_array = np.array(image_array)
        #image_array = np.true_divide(image_array,255)
        image_array = image_array.reshape(width,height,3)
        print(image_array[0][0])
        print(image_array.shape)

        class_ = vgg16.Judge(image_array)

        wordList = [class_[0][0][1]]
        wordList_json = json.dumps(wordList, ensure_ascii=False)
        return wordList_json


if __name__ == "__main__":
    #app.run(debug=True, port=8000)
    #socketio.run(app, debug=True, port=8000)
    serve(app, host='your IP address', port=8000)
