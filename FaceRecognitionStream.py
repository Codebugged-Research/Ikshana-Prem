import cv2
import mediapipe as mp

class Face_Recognition_Stream():
	def __init__(self,cap,lmain):
		self.lmain = lmain
		self.mpDraw = mp.solutions.drawing_utils
		self.mp_face_mesh = mp.solutions.face_mesh
		self.face_mesh = self.mp_face_mesh.FaceMesh()
		self.cap = cap
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
		_,frame = self.cap.read()
		if frame is not None:
			frame = cv2.resize(frame, (750, 590))
			frame = self.detect_faces(frame.copy())
			cv2.imshow('FaceRecognitionStream',frame)
			self.lmain.after(1, lambda:self.Process())