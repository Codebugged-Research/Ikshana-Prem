import cv2
import numpy as np
import os
import face_recognition
from PIL import ImageTk, Image

class Face_Recognition_Stream():
	def __init__(self,cap,lmain):
		self.lmain = lmain
		self.path  = './KnownFaces' 
		self.known_face_encodings,self.known_face_names =  self.get_known_face_encodings()
		self.cap = cap

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
		try:
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
					cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
					cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
			return frame
		except:
			return frame
	def Process(self):
		_,frame = self.cap.read()
		if frame is not None:
			frame = self.detect_faces(frame.copy())
			frame = cv2.resize(frame, (750, 590))
			cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
			img = Image.fromarray(cv2image)
			imgtk = ImageTk.PhotoImage(image=img)
			self.lmain.imgtk = imgtk
			self.lmain.configure(image=imgtk)
			self.lmain.after(1, lambda:self.Process())	