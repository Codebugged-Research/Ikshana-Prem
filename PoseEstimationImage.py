import cv2
import mediapipe as mp
import numpy as np
from PIL import ImageTk, Image
class Pose_Estimation_Image():
	def __init__(self,fd,lmain):
		self.fd = fd
		self.lmain = lmain
	def Open_File(self):
		filetypes=(('image files', '.jpeg'),('image files', '.png'),('image files', '.jpg'),)
		return self.fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)

	def Process(self):
		image = cv2.imread(self.Open_File())
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		img1 = cv2.resize(image,(250,290))
		img2 = cv2.resize(gray,(250,290))
		img2 = cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)
		divider = np.zeros((290, 250, 3), np.uint8)
		divider[:] =(200,200,200)
		image =np.concatenate((img1,img2),axis=0)
		cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=img)
		self.lmain.imgtk = imgtk
		self.lmain.configure(image=imgtk)