import csv
import cv2
import time
import imutils
import os 
from _ast import Name

cascade='haarcascade_frontalface_default.xml'
detector=cv2.CascadeClassifier(cascade)

Name=str(input("enter your name: "))
Roll_number=int(input("Enter your roll number: "))
data='dataset'
sub_data=Name
path=os.path.join(data,sub_data)

if not os.path.isdir(path):
    os.makedirs(path, exist_ok=True)
    print(sub_data)
    
info=[str(Name), str(Roll_number)]
with open('student.csv','a') as csvFile:
    write=csv.writer(csvFile)
    write.writerow(info)
csvFile.close()

print("Starting video stream...")
cam=cv2.VideoCapture(0)
time.sleep(2.0)
total=0

while total<50:
    print(total)
    _,frame=cam.read()
    img=imutils.resize(frame,width=400)
    rects=detector.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), scaleFactor=1.1,minNeighbors=5, minSize=(30,30))
    
    for (x,y,w,h) in rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        p=os.path.sep.join([path, "{}.png".format(str(total).zfill(5))])
        print("Saving images to:", os.path.abspath(path))
        cv2.imwrite(p,img)
        total +=1
        
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1) &0xFF
    if key == ord("q"):
        break 
    
cam.release()
cv2.destroyAllWindows()