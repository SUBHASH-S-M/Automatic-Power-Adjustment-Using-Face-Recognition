import streamlit as st
import pandas as pd
df=pd.read_excel("Database.xlsx",index_col=[0])
import time
time.sleep(0.02)
# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np

import os 
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
st.title("Calibration")
recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("trainer/")

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX
c=0

flag=False


print("file sucess")
image_placeholder = st.empty()

my_bar = st.progress(0)

if st.button('Start'):
    video = cv2.VideoCapture(0)
    
   

    while(True):
        ret, im = video.read()
        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        im=cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

            # Recognize the face belongs to which Id
            Id, confIdence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check the Id if exist 
            
            if(Id>0):
                name=df.iloc[Id-1,1]
                right=df.iloc[Id-1,2]
                left=df.iloc[Id-1,3]
                te= name
                print(te)
                flag=True
            

            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(te), (x,y-40), font, 1, (255,255,255), 3)
            


        # Display the video frame with the bounded rectangle

        image_placeholder.image(im)
        if(flag and c==0):
            st.title("Power Adjusting")
            
            for i in range(1,101,1):
                time.sleep(0.01)
                my_bar.progress(int(i))
            st.markdown("**Name** : "+te)
            st.markdown("**Left eye : {} D set**".format(left))
            c=1
            st.markdown("**Right eye : {} D set**".format(right))
            






