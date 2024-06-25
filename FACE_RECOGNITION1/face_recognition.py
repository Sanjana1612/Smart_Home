import cv2
import os
import time
import sys
import time
import datetime
# Import numpy for matrices calculations
import numpy as np
import time

import serial
import time
data = serial.Serial(
                    'COM9',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )
import telepot
bot=telepot.Bot('6590059318:AAHbG5S8IlG_b9BuIzDajHZmQVWIUlKOXEc')
# Create Local Binary Patterns Histograms for face recognization
##recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')
##recognizer.read('/home/pi/Desktop/face_recog_folder/Raspberry-Face-Recognition-master/trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

flag = []
count1=0
count2=0
count3=0
sample =0
lecture=0
mon=0
count=0


while True:
        now = datetime.datetime.now()

        # Read the video frame
        ret, im =cam.read()

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

            # Recognize the face belongs to which ID
            Id,i = recognizer.predict(gray[y:y+h,x:x+w])
            #id = int(os.path.split(imagePath)[-1].split(".")[1])
            
            print(i)
            # Check the ID if exist
            if i < 90:
                sample= sample+1
                if Id == 1 :
                    #flag[1]=1
                    count1=1
                    Id = "Name"
                    print("Name")
                    data.write(str.encode('A'))
                    lecture=1
                    sample=0
                    break

##                if Id == 2 :
##                    #flag[1]=1
##                    count1=1
##                    Id = "Swathi"
##                    print("Swathi")
##                    lecture=1
##                    sample=0
##                    break
##                
##                if Id == 3 :
##                    #flag[1]=1
##                    count1=1
##                    Id = "Swathi"
##                    print("Swathi")
##                    lecture=1
##                    sample=0
##                    break
##                                  
            else:
                count=count+1

                if count > 10:
                    count=0
                    print(Id)                
                    Id = "unknown"                  
                    print('UNKNOWN PERSON')
                    bot.sendMessage('1887483813',str('UNKNOWN PERSON DETECTED'))
                                     
            
            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

            # Display the video frame with the bounded rectangle
        

        cv2.imshow('im',im)
        # If 'q' is pressed, close program
        if cv2.waitKey(20) & 0xFF == ord('q'): #if cv2.waitKey(10) & 0xFF == ord('q'):
            break
           
cam.release()

# Close all windows
cv2.destroyAllWindows()
