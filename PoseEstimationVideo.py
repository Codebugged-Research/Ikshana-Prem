import cv2

class Pose_Estimation_Video():
	def __init__(self,cap,lmain):
		self.lmain = lmain
		self.cap   = cap
	def Process(self):
		_,frame = self.cap.read()
		if frame is not None:
			frame = cv2.resize(frame, (750, 590))
			frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			cv2.imshow('PoseEstimationVideo',frame)
			self.lmain.after(1, lambda:self.Process())		

