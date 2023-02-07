from tkinter import *


def Upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(3)
    statusvar.set("Ready")

root = Tk()

root.title("My Scrollbar")
root.geometry("455x233")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=Upload).pack()

root.mainloop()