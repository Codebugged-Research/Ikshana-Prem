# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:28:16 2021

@author: Harish_3055
"""

import cv2
import time
frame_rate = 2
prev = 0
fps = 0
font = cv2.FONT_HERSHEY_SIMPLEX
cap =cv2.VideoCapture('https://192.168.43.1:3055/video')
while cap.isOpened():

    time_elapsed = time.time() - prev
    res, frame = cap.read()
    
    if time_elapsed > 1./frame_rate:
        prev = time.time()
        print("hello")
        cv2.imshow('Frame',frame)
    print()
    
        
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
