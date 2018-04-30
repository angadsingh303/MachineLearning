# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 18:07:14 2018

@author: Angad Singh Toor
"""

import cv2

face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image=cv2.VideoCapture(0)

while True:
    
    _,img=image.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    dataset=face_data.detectMultiScale(gray)
    
    for x,y,w,h in dataset:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('img',img)
    
    k=cv2.waitKey(10) & 0xFF
    
    if k==27:
        break
    
image.release()
cv2.destroyAllWindows()
