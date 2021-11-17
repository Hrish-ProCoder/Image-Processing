# import packages
import cv2
import numpy as np

NAME = 'smartwatch.jpg'

# Using try except
try:
    img = cv2.imread(NAME)
    
    # Shape of image in terms of pixels.
    (rows, cols) = img.shape[:2]
    
    # Matrix Creation
    # Matrix Rotation
    Mrk = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res = cv2.warpAffine(img, M, (cols, rows))
    
    # Write img 
    cv2.imwrite('output.jpg', res)

    
except IOError:
    print ("Error while reading files")
