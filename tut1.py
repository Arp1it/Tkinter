from tkinter import *


root = Tk()

# gui logic

# width x height
root.geometry("733x433")

# width,height
root.minsize(300, 300)

# width, height
root.maxsize(900, 600)

# Label
arpit = Label(text="Arpit is a good boy and this is his GUI")
arpit.pack()

root.mainloop()