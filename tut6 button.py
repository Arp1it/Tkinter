from tkinter import *
from functools import partial
import time


def hi(h):
    if h == "hello":
        print("hello")

    if h == "hd":
        print("My name is button")

    if h == "2d":
        print("Arpit makes this programme")

    if h == "3d":
        print("hi")

    if h == "4d":
        print("exiting...")
        time.sleep(2)
        print("thanks for using.")
        exit()

root = Tk()
root.geometry("655x333")
root.title("My GUI")

ff = Frame(root, borderwidth=7, bg="grey", relief=SUNKEN)
ff.pack(side=LEFT, anchor="nw")

b1 = Button(ff, fg="white", text="Print Hello", bg="black", command=partial(hi, "hello"))
b1.pack(side=LEFT, padx=10)

b2 = Button(ff, fg="white", text="whta's your name", bg="black", command=partial(hi, "hd"))
b2.pack(side=LEFT, padx=10)

b3 = Button(ff, fg="white", text="who make this programme", bg="black", command=partial(hi, "2d"))
b3.pack(side=LEFT, padx=10)

b4 = Button(ff, fg="white", text="Print hi", bg="black", command=partial(hi, "3d"))
b4.pack(side=LEFT, padx=10)

b5 = Button(ff, fg="white", text="exit this programme", bg="black", command=partial(hi, "4d"))
b5.pack(side=LEFT, padx=10)

root.mainloop()