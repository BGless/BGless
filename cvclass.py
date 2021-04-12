import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class cvclass:

    def crt(self, upimg):
        img = cv.imread(upimg)
        gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
