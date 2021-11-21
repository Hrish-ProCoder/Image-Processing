import cv2
import numpy as np

FILE_NAME = "smartwatch.jpg"

try:
  # Read image from disk
  img = cv2.imread(FILE_NAME)
  
   # Canny Edge Detection
   edges = cv2.Canny(img, 100, 200)
   # Write image back to disk
    
   cv2.imwrite('output.jpg', edges)
