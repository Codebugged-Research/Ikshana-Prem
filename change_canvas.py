from tkinter import *
from PIL import ImageTk, Image
import numpy as np
from tkinter import filedialog as fd
import close
import cv2
from FaceRecognitionImage import Face_Recognition_Image
from FaceRecognitionVideo import Face_Recognition_Video
from FaceRecognitionStream import Face_Recognition_Stream
from PoseEstimationImage import Pose_Estimation_Image
from PoseEstimationVideo import Pose_Estimation_Video
from PoseEstimationStream import Pose_Estimation_Stream

cap   = cv2.VideoCapture(0)
lmain = None
PackageName = None
canvas = None
ls = ['Pose_Estimation','Face_Recognition','Driver_Drowsiness','Car_Damage_detection','Custom_Object_Detection','Helemet_Detection','ANPR','Rust_Detection','Work_Force_Availability','Industrial_Ocr','Mask_Detection','Fire_Detection']


def btn_clicked_event(a,heading):
	global PackageName, lmain, canvas
	PackageName = a
	canvas.itemconfig(heading, text=(' '.join(a.split('_'))))
	print("Button {} Clicked".format(a))
def close_func():
	global cap,lmain
	close.current_running_process(cap,lmain)
def video_cap():
	global PackageName,cap
	filetypes=(('video files', '.mp4'),)
	filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
	cap = cv2.VideoCapture(filename)
	getattr(globals()[PackageName+'_Video'](cap,lmain),'Process')()
def video_stream():
	global PackageName,cap
	cap = cv2.VideoCapture(0)
	getattr(globals()[PackageName+'_Stream'](cap,lmain),'Process')()


def Change_Canvas(window):
		global lmain,func_name,cap,canvas
		canvas = Canvas(
		    window,
		    bg = "#ffffff",
		    height = 856,
		    width = 1280,
		    bd = 0,
		    highlightthickness = 0,
		    relief = "ridge",)
		canvas.place(x = 0, y = 0)
		canvas.create_rectangle(0, 0, 400, 856, fill='#00203F')
		lmain = Label(canvas)
		lmain.grid()
		lmain.place(x = 600, y = 75, width=750,height=590)
		image = np.zeros((590, 750, 3), np.uint8)
		image[:] =(200,200,200)
		cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image=img)
		lmain.imgtk = imgtk
		lmain.configure(image=imgtk)
		cap = cv2.VideoCapture(0)
		img0 = PhotoImage(file = f"Button/home_page/img0.png")
		heading =canvas.create_text(
		    950, 25,
		    text = "  ",
		    fill ='#00203F',
		    font = ("HindSiliguri-Bold", int(20.0),'bold'),justify = CENTER)

		b0 = Button(
		image = img0,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[0],heading),
		relief = "flat")
		b0.place(
		x = 87, y = 750,
		width = 217,
		height = 35.15)
		img1 = PhotoImage(file = f"Button/home_page/img1.png")
		b1 = Button(
		image = img1,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[1],heading),
		relief = "flat")

		b1.place(
		x = 87, y = 690,
		width = 217,
		height = 35.15)
		img2 = PhotoImage(file = f"Button/home_page/img2.png")
		b2 = Button(
		image = img2,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[2],heading),
		relief = "flat")
		b2.place(
		x = 87, y = 620,
		width = 216,
		height = 35.15)
		img3 = PhotoImage(file = f"Button/home_page/img3.png")
		b3 = Button(
		image = img3,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[3],heading),
		relief = "flat")
		b3.place(
		x = 87, y = 550,
		width = 216,
		height = 35.15)
		img4 = PhotoImage(file = f"Button/home_page/img4.png")
		b4 = Button(
		image = img4,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[4],heading),
		relief = "flat")
		b4.place(
		x = 87, y = 480,
		width = 216,
		height = 43)
		img5 = PhotoImage(file = f"Button/home_page/img5.png")
		b5 = Button(
		image = img5,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[5],heading),
		relief = "flat")
		b5.place(
		x = 87, y = 410,
		width = 217,
		height = 38)
		img6 = PhotoImage(file = f"Button/home_page/img6.png")
		b6 = Button(
		image = img6,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[6],heading),
		relief = "flat")
		b6.place(
		x = 87, y = 355,
		width = 217,
		height = 31.1)
		img7 = PhotoImage(file = f"Button/home_page/img7.png")
		b7 = Button(
		image = img7,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[7],heading),
		relief = "flat")
		b7.place(
		x = 87, y = 270,
		width = 217,
		height = 61)
		img8 = PhotoImage(file = f"Button/home_page/img8.png")
		b8 = Button(
		image = img8,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[8],heading),
		relief = "flat")
		b8.place(
		x = 89, y = 200,
		width = 217,
		height = 55)
		img9 = PhotoImage(file = f"Button/home_page/img9.png")
		b9 = Button(
		image = img9,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[9],heading),
		relief = "flat")
		b9.place(
		x = 87, y = 150,
		width = 217,
		height = 36)
		img10 = PhotoImage(file = f"Button/home_page/img10.png")
		b10 = Button(
		image = img10,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[10],heading),
		relief = "flat")
		b10.place(
		x = 87, y = 100,
		width = 216,
		height = 34)
		img11 = PhotoImage(file = f"Button/home_page/img11.png")
		b11 = Button(
		image = img11,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:btn_clicked_event(ls[11],heading),
		relief = "flat")
		b11.place(
		x = 87, y = 50,
		width = 216,
		height = 37)
		img12 = PhotoImage(file = f"Button/home_page/img12.png")
		close_btn = Button(
		image = img12,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:close_func(),
		relief = "flat")
		close_btn.place(
		x = 1200, y = 700,
		width = 77,
		height = 76)
		img13 = PhotoImage(file = f"Button/home_page/Upload.png")
		b13 = Button(
		image = img13,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:getattr(globals()[PackageName+'_Image'](fd,lmain),'Process')(),
		relief = "flat")
		b13.place(
		x = 630, y = 700,
		width = 77,
		height = 78)
		img14 = PhotoImage(file = f"Button/home_page/webcam.png")
		b14 = Button(
		image = img14,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:video_stream(),
		relief = "flat")
		b14.place(
		x = 730, y = 700,
		width = 77,
		height = 78)
		img15 = PhotoImage(file = f"Button/home_page/VideoCam.png")
		b15 = Button(
		image = img15,
		borderwidth = 0,
		highlightthickness = 0,
		command = lambda:video_cap(),
		relief = "flat")
		b15.place(
		x = 830, y = 700,
		width = 77,
		height = 78)
		window.bind('<Escape>', lambda e: window.quit())
		window.mainloop()