import cv2
import numpy as np

cap= cv2.VideoCapture(0);  # 0 is camera number 

while True:
    ret, frame = cap.read()  #frame is image (numpy array), ret returns false if img not captured
    width = int(cap.get(3))  #width of video capture , 3 is identifier of property
    height = int(cap.get(4)) #get(4) is height
    
    image=np.zeros(frame.shape, np.uint8)     #empty image where we insert photos identical to shape of our webcam
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5 , fy=0.5) #quarter image done, we'll combine all quarter together
    image[:height//2, :width//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)  #top left
    image[height//2:, :width//2] = smaller_frame  #bottom left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  #top right
    image[height//2:, width//2:] = smaller_frame  #bottom right
    
    cv2.imshow('frame', image)
    
    if(cv2.waitKey(1)==ord('q')):  #if we press q, it stops , else not
        break

cap.release()
cv2.destroyAllWindows()