from tkinter import *
import time


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x344")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button Clicked")
        self.var.set("updating...")
        self.statusbar.update()
        time.sleep(3)
        self.var.set("Done!!")
        self.statusbar.update()
        time.sleep(2)
        self.var.set("Ready")

    def createbutton(self, inputt):
        Button(text=inputt, command=self.click).pack()

if __name__=="__main__":
    window = GUI()
    window.status()
    window.createbutton("Hello please click me!")
    window.mainloop()