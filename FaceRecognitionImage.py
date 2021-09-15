import cv2
import numpy as np
import os
import face_recognition
from PIL import ImageTk, Image
class Face_Recognition_Image():
	def __init__(self,fd,lmain):
		self.fd = fd
		self.lmain = lmain
		self.path  = './KnownFaces' 
		self.known_face_encodings,self.known_face_names =  self.get_known_face_encodings()
	def Open_File(self):
		filetypes=(('image files', '.jpeg'),('image files', '.png'),('image files', '.jpg'),)
		return self.fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
	def get_known_face_encodings(self):
		ls = os.listdir(self.path)
		known_face_encodings = []
		known_face_names = []
		for i in ls:
		    name,extension = i.split('.')
		    if extension in ['jpeg','jpg','png']:
		        me = face_recognition.load_image_file(self.path+'/'+i)
		        face = face_recognition.face_encodings(me)[0]
		        known_face_encodings.append(face)
		        known_face_names.append(name)
		return known_face_encodings,known_face_names
	def detect_faces(self,frame):
		# try:
			small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
			rgb_small_frame = small_frame[:, :, ::-1]
			face_locations = face_recognition.face_locations(rgb_small_frame)
			face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
			face_names = []
			for encodeFace, faceLoc in zip(face_encodings, face_locations):
				matches = face_recognition.compare_faces(self.known_face_encodings, encodeFace)
				faceDis = face_recognition.face_distance(self.known_face_encodings, encodeFace)
				matchIndex = np.argmin(faceDis)
				if matches[matchIndex]:
					name = self.known_face_names[matchIndex].upper()
					y1, x2, y2, x1 = faceLoc
					y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
					cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 8)
					cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 6)
				else:
					y1, x2, y2, x1 = faceLoc
					y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
					cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 8)
					cv2.putText(frame, 'Unknown', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 6)
			return frame
		# except:
		# 	print('Error')
		# 	return frame
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
		