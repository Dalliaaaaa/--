"""
#only width

import cv2

img = cv2.imread('python_opencv/images/test1.jpg',cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

width = 440
height = img.shape[0]
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print("Resized Dimensions : ",resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#only height

import cv2

img = cv2.imread('python_opencv/images/test1.jpg',cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

width = img.shape[1]
height = 440
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print("Resized Dimensions : ",resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()