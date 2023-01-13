import cv2

#준비
cascade_file = 'haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)

#검출하기
img = cv2.imread('python_opencv/images/face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #흑백변환
face_list = cascade.detectMultiScale(gray,minSize = (10, 10)) #얼굴 검출

for (x, y, w, h) in face_list:
    color = (255, 0, 0)
    pen_w = 2
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w)

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.imwrite('temp.jpg', img)

cv2.waitKey()
cv2.destroyAllWindows()