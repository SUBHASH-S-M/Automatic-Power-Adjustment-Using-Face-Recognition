####################################################
# Modified by Nazmi Asri                           #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Import OpenCV2 for image processing
import cv2
import os

# Start capturing video
vid_cam = cv2.VideoCapture(0)
vid_cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# Detect object in video stream using Haarcascade Frontal Face
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, one face id
face_id =input("Enter the name :")

# Initialize sample face image
count = 0
path ='E:\Project_subhash\mp\dataset\\'+face_id

# Check whether the specified path exists or not
isExist = os.path.exists(path)

if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(path)
  print("The new directory is created!")


# Start looping
while(True):

    # Capture video frame
    _, image_frame = vid_cam.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

    # Detect frames of different sizes, list of faces rectangles
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # Loops for each faces
    for (x,y,w,h) in faces:

        # Crop the image frame into rectangle
        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)

        # Increment sample face image
        

        # Save the captured image into the datasets folder
        #cv2.imwrite("path/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imwrite(os.path.join(path ,str(face_id) + '.' + str(count)+".jpg"), gray[y:y+h,x:x+w])
        
        print(count)

        # Display the video frame, with bounded rectangle on the person's face
        cv2.imshow('frame', image_frame)

    # To stop taking video, press 'q' for at least 100ms
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    # If image taken reach 100, stop taking video
    elif count==100:
        break


# Stop video
vid_cam.release()

# Close all started windows
cv2.destroyAllWindows()
