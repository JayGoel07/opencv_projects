# Open CV : Open Source computer Vision lubrary used for image analysis,facial recogniton, object detection etc., extension is as folows
import cv2   
import random
 
img = cv2.imread('assets/DIL_SE.png', 1)  # -1 : Colorful image, 0 : black and white, 1 : original
print(type(img))                          # <class 'numpy.ndarray'>  , its a numpy array of RGB values
print(img.shape)                          # (312,315,3) ~ (no of rows[height], no of columns[width], no of channels[B-G-R in open-cv ]), 0 is black

for i in range(70):                       # Modify pixel values of image
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]
tag = img[150:200,150:200]                # copy part of image and past anywhere else
img[0:50,0:50] = tag
        
img = cv2.resize(img, (400,400))          # Resize the image into 400*400 pixels
#img = cv2.resize(img, (0,0), fx=0.5 , fy=0.5) #Reduce the image into half by fractions or double it
#img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Image', img)                  #label for image



cv2.waitKey(0)   #wait infiintie time unless we press a key, a number : numerb  secs ke bd move on
cv2.destroyAllWindows()