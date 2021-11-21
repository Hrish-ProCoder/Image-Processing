import cv2
import numpy as np

FILE_NAME = "smartwatch.jpg"

try:
  # Read image from disk
  img = cv2.imread(FILE_NAME)
   # Canny Edge Detection
    
