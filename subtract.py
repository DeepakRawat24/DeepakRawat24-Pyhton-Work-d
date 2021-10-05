import cv2
import numpy as np

img1 = cv2.imread('sec.jpg')
img2 = cv2.imread('demo.jpg')

# subtract
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
sub = cv2.subtract(img1, img2_resized)
cv2.imshow('Image sub', sub)

cv2.waitKey(0)
cv2.destroyAllWindows()