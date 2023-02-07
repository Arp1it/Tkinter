from tkinter import *


def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1

i = 0

root = Tk()

root.title("My List Box")
root.geometry("455x233")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item in my listbox")

Button(root, text="ADD item", command=add).pack()

root.mainloop()