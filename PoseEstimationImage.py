import cv2
import numpy as np
import mediapipe as mp
from PIL import ImageTk, Image
class Pose_Estimation_Image():
	def __init__(self,fd,lmain):
		self.fd = fd
		self.lmain = lmain
		self.lmain = lmain
		self.mp_drawing = mp.solutions.drawing_utils
		self.mp_pose = mp.solutions.pose
		self.pose = self.mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)
	def Open_File(self):
		filetypes=(('image files', '.jpeg'),('image files', '.png'),('image files', '.jpg'),)
		return self.fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
	def detect_pose(self,frame):
		try:
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			results = self.pose.process(frame)
			frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
			self.mp_drawing.draw_landmarks(frame,results.pose_landmarks,self.mp_pose.POSE_CONNECTIONS)
			return frame
		except:
			return frame
	def Process(self):
		image = cv2.imread(self.Open_File())
		self.detected_frame = self.detect_pose(image.copy())
		img1 = cv2.resize(image,(250,290))
		img2 = cv2.resize(self.detected_frame,(250,290))
		divider = np.zeros((290, 250, 3), np.uint8)
		divider[:] =(200,200,200)
		image =np.concatenate((img1,img2),axis=0)
		cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=img)
		self.lmain.imgtk = imgtk
		self.lmain.configure(image=imgtk)
		