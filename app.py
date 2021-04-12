import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt
import cvclass 
from flask import Flask, render_template
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/remove", methods=["POST"])
def remove():

    start = time.time()

    if 'file' not in request.files:
        return jsonify({'error': 'missing file'}), 400

    if request.files['file'].filename.rsplit('.', 1)[1].lower() not in ["jpg", "png", "jpeg"]:
        return jsonify({'error': 'invalid file format'}), 400

    data = request.files['file'].read()
    
    if len(data) == 0:
        return jsonify({'error': 'empty image'}), 400

    img = Image.open(io.BytesIO(data))
    remove = cvclass.crt(img)
    return remove


