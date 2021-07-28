from tkinter import *
import numpy as np
import cv2
from PIL import ImageTk, Image

index = 1
def btn_clicked(a):
    global index
    global cap
    print("Button {} Clicked".format(a))
    if a=='close':
        video_stream(0)
    else:
        cap = cv2.VideoCapture(0)
        video_stream(1)


window = Tk()
window.state("zoomed")
# window.geometry("1280x800")
window.configure(bg = "#ffffff")

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 856,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    )
canvas.place(x = 0, y = 0)

canvas.create_rectangle(0, 0, 400, 856, fill='#00203F')
img0 = PhotoImage(file = f"Button/home_page/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:btn_clicked(12),
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
    command = lambda:btn_clicked(11),
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
    command = lambda:btn_clicked(10),
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
    command = lambda:btn_clicked(9),
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
    command = lambda:btn_clicked(8),
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
    command = lambda:btn_clicked(7),
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
    command = lambda:btn_clicked(6),
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
    command = lambda:btn_clicked(5),
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
    command = lambda:btn_clicked(4),
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
    command = lambda:btn_clicked(3),
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
    command = lambda:btn_clicked(2),
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
    command = lambda:btn_clicked(1),
    relief = "flat")


b11.place(
    x = 87, y = 50,
    width = 216,
    height = 37)

img12 = PhotoImage(file = f"Button/home_page/img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:btn_clicked('close'),
    relief = "flat")


b12.place(
    x = 900, y = 700,
    width = 77,
    height = 76)




lmain = Label(canvas)
lmain.grid()
lmain.place(x = 600, y = 50, width=750,height=590)
# Capture from camera
cap = cv2.VideoCapture(0)
# function for video streaming
def video_stream(index):
    try:
        if index == 1:
            _, frame = cap.read()
            frame = cv2.resize(frame, (750, 590))
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(1, lambda:video_stream(1))
        else:
            cap.release()
            cv2.destroyAllWindows()
            image = np.zeros((590, 750, 3), np.uint8)
            image[:] =(255,255,255)
            cv2image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)

    except :
            pass
window.resizable(False, False)
window.mainloop()