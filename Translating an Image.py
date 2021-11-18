import cv2
import numpy as np
FILE = 'smartwatch.jpg'
M = np.float32([[1, 0, 100], [0, 1, 50]])

try:
  img = cv2.imread(FILE)
