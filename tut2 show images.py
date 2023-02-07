from tkinter import *
from PIL import Image, ImageTk


root = Tk()

root.geometry("455x244")
# photoo = PhotoImage(file="stadium.jpg")
photoo = PhotoImage(file="dinaso.png")

label = Label(image=photoo)
label.pack()

# For jpg images
image = Image.open("stadium.jpg")
photo1 = ImageTk.PhotoImage(image)

label = Label(image=photo1)
label.pack()

root.mainloop()