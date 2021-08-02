import cv2
import mediapipe as mp
import numpy as np
from PIL import ImageTk, Image
class Face_Recognition_Image():
	def __init__(self,fd,lmain):
		self.fd = fd
		self.lmain = lmain
		self.mpDraw = mp.solutions.drawing_utils
		self.mp_face_mesh = mp.solutions.face_mesh
		self.face_mesh = self.mp_face_mesh.FaceMesh()
	def Open_File(self):
		filetypes=(('image files', '.jpeg'),('image files', '.png'),('image files', '.jpg'),)
		return self.fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
	def detect_faces(self,frame):
		try:
			results = self.face_mesh.process(frame)
			if results.multi_face_landmarks and frame is not None:
				for faceLms in results.multi_face_landmarks:
					h, w, c = frame.shape
					cx_min=  w
					cy_min = h
					cx_max= cy_max= 0
					for id, lm in enumerate(faceLms.landmark):
						cx, cy = int(lm.x * w), int(lm.y * h)
						if cx<cx_min:
							cx_min=cx
						if cy<cy_min:
							cy_min=cy
						if cx>cx_max:
							cx_max=cx
						if cy>cy_max:
							cy_max=cy
					cv2.rectangle(frame, (cx_min, cy_min), (cx_max, cy_max), (255, 255, 0), 2)
			return frame
		except:
			return frame
	def Process(self):
		image = cv2.imread(self.Open_File())
		self.detected_frame = self.detect_faces(image.copy())
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
		