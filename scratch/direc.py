import os
face_id="Subhas1"
path ='E:\Project_subhash\mp\dataset\{}'.format(face_id+"\\")
isExist = os.path.exists(path)
if not isExist:
  # Create a new directory because it does not exist 
  os.makedirs(path)
  print(path)
  print("The new directory is created!")
  