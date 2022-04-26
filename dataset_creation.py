from numpy import float_power
import streamlit as st
import cv2
import os
import pandas as pd
df=pd.read_excel("Database.xlsx",index_col=[0])

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
st.title("Face Registration")
video = cv2.VideoCapture(0)
face_id=st.text_input("Enter the Name ")
right=st.text_input("ENter the right eye power","(D)")
left=st.text_input("ENter the left eye power","(D)")


image_placeholder = st.empty()



if st.button('Start'):
    df.loc[len(df.index)] = [len(df)+1,face_id,float(right),float(left)] 
    df.to_excel("Database.xlsx")

    path ='E:\Project_subhash\mp\dataset\\'
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print("The new directory is created!")
    my_bar = st.progress(0)

    count=1
    while(True):
        success, image = video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
            cv2.imwrite(path+"{}_{}.jpg".format(face_id,count),gray[y:y+h,x:x+w]) 
            count+=1
            my_bar.progress((count))
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_placeholder.image(image)
        if(count>=100):
            st.text("Registration Completed")
            break
    video.release()
if st.button('Abort'):
    video.release()