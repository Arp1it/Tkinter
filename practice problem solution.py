from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Arpit GUI")
root.geometry("455x244")

ar = Label(text="Times of India", font="bold 30")
ar.pack()

date1 = Label(text="11/8/2022", font="10", fg = "white", bg="black")
date1.pack(side=RIGHT, anchor=NE)

photo1 = Image.open("download.jpg")
img = ImageTk.PhotoImage(photo1)

labell = Label(image=img)
labell.pack(side = LEFT, anchor=NW)

photo12 = Image.open("news1.webp")
img1 = ImageTk.PhotoImage(photo12)

labelll = Label(image=img1)
labelll.pack(side = RIGHT, anchor=NE)

photo123 = Image.open("news2.jpg")
img12 = ImageTk.PhotoImage(photo123)

labelll1 = Label(image=img12)
labelll1.pack(side= TOP)

photo1234 = Image.open("download1.jpg")
img123 = ImageTk.PhotoImage(photo1234)

labelll12 = Label(image=img123)
labelll12.pack(side = BOTTOM)

root.mainloop()