
import cv2
import numpy as np

NAME = 'smartwatch.jpg'
try:
    img = cv2.imread(NAME)
    
    # Shape of image in terms of pixels.
