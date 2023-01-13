import cv2

img = cv2.imread('images/test1.jpg')

cv2.imshow('image',img) #이미지 보여줌
cv2.waitKey() #버튼 눌릴 때까지 기다림
cv2.destroyAllWindows() #떴던 이미지창 지우기