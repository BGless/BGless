import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')




