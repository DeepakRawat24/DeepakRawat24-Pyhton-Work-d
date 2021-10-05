import cv2
import numpy as np

img1 = cv2.imread('sec.jpg')
img2 = cv2.imread('demo.jpg')

# multiply
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
mul = cv2.multiply(img1,1.2, img2_resized,1.8)
cv2.imshow('Image sub', mul)

cv2.waitKey(0)
cv2.destroyAllWindows()