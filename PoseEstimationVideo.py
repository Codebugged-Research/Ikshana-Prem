import cv2
import numpy as np
from PIL import ImageTk, Image
class Pose_Estimation_Video():
	def __init__(self,cap,lmain):
		self.lmain = lmain
		self.cap   = cap
	def Process(self):
		_,frame = self.cap.read()
		if frame is not None:
			frame = cv2.resize(frame, (750, 590))
			frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
			img = Image.fromarray(cv2image)
			imgtk = ImageTk.PhotoImage(image=img)
			self.lmain.imgtk = imgtk
			self.lmain.configure(image=imgtk)
			self.lmain.after(1, lambda:self.Process())		
