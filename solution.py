from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("My GUI")

ar = Label(text="Ready", font="bold 15", bg="black", fg="white")
ar.pack(side=BOTTOM, fill=X)

root.mainloop()