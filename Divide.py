import cv2
import numpy as np

img1 = cv2.imread('image/sec.jpg')
# img2 = cv2.imread('image/demo.jpg')

# divide
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
div = cv2.divide(img1, img2_resized)
cv2.imshow('Image div', div)

cv2.waitKey(0)
cv2.destroyAllWindows()
