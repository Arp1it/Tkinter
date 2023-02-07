from tkinter import *

root = Tk()

root.geometry("655x333")
root.title("My GUI")

f1 = Frame(root, bg = "grey", borderwidth=7, relief=SUNKEN)
f1.pack(side = LEFT, fill=Y)

l = Label(f1, text="Project tkinter - VS CODE")
l.pack(pady=142)

f2 = Frame(root, bg = "grey", borderwidth=9, relief=SUNKEN)
f2.pack(side = TOP, fill=X)

l = Label(f2, text="Welcome to sublime text", font="Helvetica 10 bold")
l.pack(padx=142, pady=20)

root.mainloop() 