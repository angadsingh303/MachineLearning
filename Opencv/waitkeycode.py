Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import cv2


>>> 
>>> cv2.waitKey()
-1
>>> cv2.waitKey(10)
-1
>>> cv2.waitKey(10) &0xFF
255
>>> cv2.waitKey(10) &0xAA
170
>>> 
