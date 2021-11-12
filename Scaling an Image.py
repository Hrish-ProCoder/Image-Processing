import cv2
import numpy as np
name = 'smartwatch.jpg'
try:
  img = cv2.imread(name)
  (height, width) = img.shape[:2]
  res = cv2.resize(img, (int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)
  cv2.imwrite('outputimg.jpg', res)
  
except IOError:
  print("Error while reading the file")
