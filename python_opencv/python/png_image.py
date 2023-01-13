import cv2

img = cv2.imread('python_opencv\images\Kakao_lion.png', cv2.IMREAD_UNCHANGED)

print(img[100][50])