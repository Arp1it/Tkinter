from tkinter import *


root = Tk()

root.minsize(600, 500)

def getval():
    a = user_in.get()
    b = user_hein.get()

    root.geometry(f"{a}x{b}")

root.geometry("800x800")

head = Label(text="Window Resizer", font="bold 30").grid(row=0, column=7)

window_width = Label(text="Windows Width").grid(row=1, column=0)
window_height = Label(text="Windows Height").grid(row=2, column=0)

user_in = StringVar()
user_hein = StringVar()

user_inp = Entry(root, textvariable=user_in).grid(row=1, column=2)
user_heinp = Entry(root, textvariable=user_hein).grid(row=2, column=2)

Button(text="Apply", command=getval).grid(row=4, column=6)

root.mainloop()