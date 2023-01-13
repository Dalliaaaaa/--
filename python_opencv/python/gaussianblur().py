import cv2
import numpy
src = cv2.imread('python_opencv/images/Kakao_lion.png', cv2.IMREAD_UNCHANGED)

dst = cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)

cv2.imshow("Guassian Smoothing", numpy.hstack())
cv2.waitKey()
cv2.destroyAllWindows()