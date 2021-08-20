# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 16:09:59 2021

@author: Harish_3055
"""

## METHOD 1
##Capture will be stopped @ 100th frame

import cv2
cap = cv2.VideoCapture(0)
FrameCount = 100
Count = 0
while cap.isOpened():
    _,frame = cap.read()
    Count+=1
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) == ord('q') or FrameCount==Count:
        break
cv2.destroyAllWindows()
cap.release()
##



##METHOD 2
## Frame will be skipped in range 100 - 200

import cv2
cap = cv2.VideoCapture(0)
Count=0
FrameRange=list(range(100,200))
while True:
    if Count not in range(100,200):
        _,frame = cap.read()
        cv2.imshow('Frame',frame)
    else:
        cv2.destroyAllWindows()
    if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break
    Count+=1
##