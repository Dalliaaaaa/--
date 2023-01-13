import numpy as np
import cv2

xml = 'haarcascade_frontalface_default.xml' # 얼굴 인식파일 불러오기
face_cascade = cv2.CascadeClassifier(xml) # 화면에서 얼굴 인식하는 변수

cap = cv2.VideoCapture(0) # 비디오 캡쳐
cap.set(3,640) # 너비
cap.set(4,480) # 높이

while(True):
    ret, frame = cap.read() # 웹캠 캡쳐 불러오기
    frame = cv2.flip(frame, 1) # 좌우 대칭
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.05, 5)
    print("Number of faces detected: "+ str(len(faces)))

    if len(faces):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('result',frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # Esc 키를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()
