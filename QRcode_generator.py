import qrcode
from tkinter import *

qr = Tk()
qr.title('qrcodegenerator')
qr.geometry('700x250')
qr.config(bg='#06c8d6')

def generate():
    img = qrcode.make(msg.get())
    type(img)
    img.save(f'{save_name.get()}.png')
    Label(qr, text='File Saved!', bg='#06c8d6' , fg='black', font=('Arial Black', 8)).pack()

def show():
    img = qrcode.make(msg.get())
    type(img)
    img.show()

frame = Frame(qr, bg='#06c8d6')
frame.pack(expand=True)

#NTER THE TEXT OR URL

Label(frame, text='Enter the Text or URL : ', font=('Arial Black', 16),
      bg='#06c8d6').grid(row=0, column=0, sticky='w')

msg = Entry(frame)
msg.grid(row=0, column=1)

#ENTER THE FILE NAME

Label(frame, text='File Name(Save As) : ', font=('Arial Black', 16),
      bg='#06c8d6').grid(row=1, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=1, column=1)

#BUTTONS TO SHOW OR SAVE QRCODE

btn = Button(qr, text='Show QR code', bd='5', command=show, width=15)
btn.pack()
btn = Button(qr, text='Save QR code', command=generate, bd='5', width=15)
btn.pack()
qr.mainloop()