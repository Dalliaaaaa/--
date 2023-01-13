import cv2

img =cv2.imread('python_opencv\images\Kakao_lion.png')
edges = cv2.Canny(img,100,200)

cv2.imshow("Edge Detected Image", edges)

cv2.waitKey()
cv2.destroyAllWindows()