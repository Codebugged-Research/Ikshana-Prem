import cv2
import numpy as np
import mediapipe as mp
from PIL import ImageTk, Image
class Pose_Estimation_Video():
	def __init__(self,cap,lmain):
		self.lmain = lmain
		self.mp_drawing = mp.solutions.drawing_utils
		self.mp_pose = mp.solutions.pose
		self.pose = self.mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)
		self.cap = cap
	def detect_pose(self,frame):
		try:

			frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
			results = self.pose.process(frame)
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
			self.mp_drawing.draw_landmarks(frame,results.pose_landmarks,self.mp_pose.POSE_CONNECTIONS)
			return frame
		except:
			return frame
	def Process(self):
		_,frame = self.cap.read()
		if frame is not None:
			frame = self.detect_pose(frame.copy())
			frame = cv2.resize(frame, (750, 590))
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
			img = Image.fromarray(cv2image)
			imgtk = ImageTk.PhotoImage(image=img)
			self.lmain.imgtk = imgtk
			self.lmain.configure(image=imgtk)
			self.lmain.after(1, lambda:self.Process())	