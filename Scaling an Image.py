import cv2
import numpy as np
name = 'smartwatch.jpg'
try:
  img = cv2.imread(name)
  (height, width) = img.shape[:2]
  
