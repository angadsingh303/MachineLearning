# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 18:20:13 2018

@author: Angad Singh Toor
"""

import cv2

face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image=cv2.imread('image_1.jpg',cv2.IMREAD_COLOR)
# Scale factor - 1.3  -  reduced  to 30%
dataset=face_data.detectMultiScale(image,1.3)

for x,y,w,h in dataset:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2#border-width)
    
cv2.imwrite('result.jpg',image)
    