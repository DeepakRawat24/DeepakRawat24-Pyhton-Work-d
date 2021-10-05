import cv2
import numpy as np

img1 = cv2.imread('sec.jpg')
img2 = cv2.imread('demo.jpg')

# addition
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
add = cv2.addWeighted(img1, 0.5, img2_resized, 0.4, 0)
cv2.imshow('Image', add)

cv2.waitKey(0)
cv2.destroyAllWindows()