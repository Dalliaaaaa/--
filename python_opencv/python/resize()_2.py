#upscale

import cv2

img = cv2.imread('python_opencv/images/test1.jpg', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ',img.shape)

scale_parcent = 220
width = int(img.shape[1] * scale_parcent / 100)
height = int(img.shape[0] * scale_parcent /100)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
