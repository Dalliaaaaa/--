import cv2

grey_img = cv2.imread('python_opencv/images/test1.jpg', cv2.IMREAD_GRAYSCALE) #회색조 모드에서 이미지를 로드

status = cv2.imwrite('python_opencv/images/test1.jpg', grey_img) #이미지를 저장

print("Image written to file-system : ", status) #지정된 경로에 성공적으로 기록되면 True를 반환