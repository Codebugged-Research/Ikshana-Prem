import cv2
import numpy as np
from PIL import ImageTk, Image
class Custom_Object_Detection_Stream():
	def __init__(self,cap,lmain):
		self.lmain = lmain
		self.cap = cap
		self.net = cv2.dnn.readNet("tiny/yolov4-tiny.weights", "tiny/yolov4-tiny.cfg")
		self.classes = []
		with open("tiny/coco.names", "r") as f:
		    self.classes = [line.strip() for line in f.readlines()]
		self.layer_names = self.net.getLayerNames()
		self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
		self.colors = np.random.uniform(0, 255, size=(1, 3))
	def Open_File(self):
		filetypes=(('image files', '.jpeg'),('image files', '.png'),('image files', '.jpg'),)
		return self.fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
	def fun(self,img,outs,width,height,channels):
	    class_ids = []
	    confidences = []
	    boxes = []
	    for out in outs:
	        for detection in out:
	            scores = detection[5:]
	            class_id = np.argmax(scores)
	            confidence = scores[class_id]
	            if confidence > 0.5:
	                center_x = int(detection[0] * width)
	                center_y = int(detection[1] * height)
	                w = int(detection[2] * width)
	                h = int(detection[3] * height)
	                x = int(center_x - w / 2)
	                y = int(center_y - h / 2)
	                boxes.append([x, y, w, h])
	                confidences.append(float(confidence))
	                class_ids.append(class_id)
	    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.5)  
	    font = cv2.FONT_HERSHEY_PLAIN
	    for i in range(len(boxes)):
	        if i in indexes:
	            x, y, w, h = boxes[i]
	            label = str(self.classes[class_ids[i]])
	            color = self.colors[0]
	            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
	            cv2.putText(img, label, (x, y - 10), font, 3, color, 3)
	    
	    return img
	def Process(self):
		_,frame = self.cap.read()
		if frame is not None:
			height, width, channels = frame.shape
			blob = cv2.dnn.blobFromImage(frame, 0.00392, (640, 480), (0, 0, 0), True, crop=False)
			self.net.setInput(blob)
			outs = self.net.forward(self.output_layers)
			result = self.fun(frame.copy(),outs,width,height,channels)
			result = cv2.resize(result, (750, 590))
			cv2image = cv2.cvtColor(result, cv2.COLOR_BGR2RGBA)
			img = Image.fromarray(cv2image)
			imgtk = ImageTk.PhotoImage(image=img)
			self.lmain.imgtk = imgtk
			self.lmain.configure(image=imgtk)
			self.lmain.after(10, lambda:self.Process())