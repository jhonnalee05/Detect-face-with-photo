import numpy as np 

import cv2

import os 
def get_filepaths(directory) :
  file_paths= [] #lista que almacenara las rutas 
#crear rutas 
  for root, directories, files in os.walk(directory):
   for filename in files:
     filepath = os.path.join(root, filename )
     file_paths.append(filepath)
  return file_paths
full_file_paths =get_filepaths("imagenesInput")

face_cascade =cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt.xml')
eye_cascade =cv2.CascadeClassifier('haarcascades\haarcascade_eye.xml')

i=1

for path in full_file_paths:
  print(path)
  img=cv2.imread(path)
  gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
  faces=face_cascade.detectMultiScale(gray, 1.3, 5)
  
  for(x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h) ,(125,255,0),2)
     rol_gray = gray[y:y+h,x:x+w]
     rol_color = img[y:y+h,x:x+w]
   
     eyes=eye_cascade.detectMultiScale(rol_gray)
   
     for(ex,ey,ew,eh) in eyes:
      cv2.rectangle(rol_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
     
  cv2.imshow('img'+ str(i),img)
  cv2.imwrite("imagenesOutput/img-"+str(i) +".jpg",img)
  i    = 1    +   1  
   
     