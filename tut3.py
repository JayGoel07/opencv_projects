import numpy as np 
import cv2

cap  = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')  #for face detection classfier
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_eye.xml') 

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #gray scale
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  #location of all faces[rectangles] | 1.30-> shrink the image by 30% but faster algorithm | how accurately this algorithm need to be (3-6 value rhti h)
    # last parameter affects the quality of the image , you dont want to detect faces that are 1/4th size of image 
    
    for(x,y,w,h) in faces :
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 5)  #(frame, top left, bottom right, color, thickness of line)
        #need to face exaclty to find eyes , roi: region of interest
        roi_grey= gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_grey, 1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5)
        
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1)==ord('b'):
        break
    
cap.release()
cv2.destroyAllWindows()