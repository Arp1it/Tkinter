import os 
from tkinter import *
from PIL import Image, ImageTk


root = Tk()
os.chdir("F:\\")
b = os.listdir("F:\\")
# print(b)
ar = Label(text="My name is Label")
ar.pack()

phooto = PhotoImage(file="1.png")
labell = Label(image=phooto)
labell.pack()

photo2 = Image.open("stand.jpg")
image = ImageTk.PhotoImage(photo2)

labe = Label(image=image)
labe.pack()

root.mainloop()