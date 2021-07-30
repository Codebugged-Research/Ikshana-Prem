from tkinter import *
from PIL import ImageTk, Image

#Button function starts
def btn_clicked():
    global entry1
    global entry0
    print('User_ID : ',entry1.get())
    print('Password: ',entry0.get())
    if entry1.get() == 'Harish' and entry0.get() == 'harish@123':
    	window.destroy()
    	import Home_page
    else:
    	canvas.itemconfig(tagOrId='error', text = 'Invaid Credentials :)')

    print("Button Clicked")
#Button function ends

def handle_click_entry0(event):
    global entry0
    global canvas
    change = StringVar(canvas, value='')
    entry0.config(show='*',textvariable = change)

def handle_click_entry1(event):
    global entry1
    global canvas
    change = StringVar(canvas, value='')
    entry1.config(textvariable = change)   


window = Tk()
window.state("zoomed")
window.title('Ikshana Application')
ico = Image.open('Button/login_page/logo_icon.jpg')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
# window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1000,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

logo = ImageTk.PhotoImage((Image.open("Button/login_page/vector.png")).resize((832,1000), Image.ANTIALIAS))
logo_bg = canvas.create_image(400, 450,image = logo)

entry0_img = PhotoImage(file = f"Button/login_page/img_textBox0.png")
entry0_bg = canvas.create_image(
    1200.0, 479,
    image = entry0_img)

default_text_password = StringVar(canvas, value='Password')

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    font = ('calibre',15,'normal'),
    highlightthickness = 0,
    textvariable = default_text_password,)

entry0.place(
    x = 1010.0, y = 450,
    width = 382.0,
    height = 55)
entry0.bind("<1>", handle_click_entry0)



entry1_img = PhotoImage(file = f"Button/login_page/img_textBox1.png")
entry1_bg = canvas.create_image(
    1200.0, 371.9,
    image = entry1_img)

default_text_user = StringVar(canvas, value='User_ID')

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    font = ('calibre',15,'normal'),
    highlightthickness = 0,
    textvariable = default_text_user)


entry1.place(
    x = 1010.0, y = 345,
    width = 382.0,
    height = 55)

entry1.bind("<1>", handle_click_entry1)


img0 = PhotoImage(file = f"Button/login_page/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 1130, y = 600,
    width = 132,
    height = 44)


sample = PhotoImage(file = f"Button/login_page/Image.png")
robo_img = canvas.create_image(
    1200.0, 200,
    image = sample)


canvas.create_text(
    1190.0, 300.5,
    text = "  Sign in",
    fill = "#4e6fe7",
    font = ("HindSiliguri-Bold", int(20.0),'bold'))

canvas.create_text(
    1190, 700.0,
    text = "Copyright ©2021 Codebugged. All Rights Reserved",
    fill = "#000000",
    font = ("Roboto-Thin", int(12.0)))

err_msg = canvas.create_text(
	1110, 550,
    text = "",
    fill = "Red",
    font = ("Roboto-Thin", int(18.0)),
    tag  = 'error')


window.resizable(False, False)
window.mainloop()