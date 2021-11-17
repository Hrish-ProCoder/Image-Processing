
import cv2
import numpy as np

NAME = 'smartwatch.jpg'
try:
    img = cv2.imread(NAME)
    
    # Shape of image in terms of pixels.
    (rows, cols) = img.shape[:2]
    
    # Matrix Creation
    # Matrix Rotation
    Mrk = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
