from tkinter import *


def arpit(event):
    print(f"You clicked on the button at {event.x}, {event.y}")

root = Tk()

root.title("Events in Tkinter")
root.geometry("644x334")

widgit = Button(root, text="Click me please")
widgit.pack()

widgit.bind('<Button-1>', arpit)
widgit.bind('<Double-1>', quit)

root.mainloop()