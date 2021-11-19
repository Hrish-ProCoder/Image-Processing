import cv2
import numpy as np
FILE = 'smartwatch.jpg'
M = np.float32([[1, 0, 100], [0, 1, 50]])

# try block
try:
  # read image
  img = cv2.imread(FILE)
  (rows, cols) = img.shape[:2]
  
  # warpAffine - does appropriate shifting given in the translation matrix
  res = cv2.warpAffine(img, M, (cols, rows))
  #write image
  cv2.imwrite('output.jpg', res)
  
# except block
except IOError:
  print ("Error while reading files")
