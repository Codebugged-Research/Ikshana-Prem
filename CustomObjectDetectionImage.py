import cv2
import numpy as np
from PIL import ImageTk, Image
class Custom_Object_Detection_Image():
	def __init__(self,fd,lmain):
		self.fd = fd
		self.lmain = lmain
		self.net = cv2.dnn.readNet("tiny/yolov4-tiny.weights", "tiny/yolov4-tiny.cfg")
		self.classes = []
		with open("tiny/coco.names", "r") as f:
		    self.classes = [line.strip() for line in f.readlines()]
		self.layer_names = self.net.getLayerNames()
		self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
		self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
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
	            if confidence > 0:
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
	            color = self.colors[i]
	            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
	            cv2.putText(img, label, (x, y - 10), font, 3, color, 3)
	    
	    return img
	def Process(self):
		image = cv2.imread(self.Open_File())
		height, width, channels = image.shape
		blob = cv2.dnn.blobFromImage(image, 0.00392, (640, 480), (0, 0, 0), True, crop=False)
		self.net.setInput(blob)
		outs = self.net.forward(self.output_layers)
		result = self.fun(image.copy(),outs,width,height,channels)
		img1 = cv2.resize(image,(250,290))
		img2 = cv2.resize(result,(250,290))
		divider = np.zeros((290, 250, 3), np.uint8)
		divider[:] =(200,200,200)
		image =np.concatenate((img1,img2),axis=0)
		cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=img)
		self.lmain.imgtk = imgtk
		self.lmain.configure(image=imgtk)