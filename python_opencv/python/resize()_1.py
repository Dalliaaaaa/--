#downscale

import cv2

img = cv2.imread('python_opencv/images/test1.jpg', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

scale_percent = 60 #이미지 규모 퍼센트 60으로 지정
width = int(img.shape[1] * scale_percent / 100) #원래 이미지 너비 * 규모 60퍼센트 값의 정수부분을 너비로 지정
height = int(img.shape[0] * scale_percent / 100) #원래 이미지 높이 * 규모 60퍼센트 값의 정수부분을 높이로 지정
dim = (width, height) #너비와 높이 dim에 저장

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) #resized image

print('Resized Dimensions : ', resized.shape) #resized image 규모 출력

cv2.imshow("Resized image", resized) #resized image 창에 띄움
cv2.waitKey(0)
cv2.destroyAllWindows()