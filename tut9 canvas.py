from tkinter import *


root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Arpit's GUI")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# making a line from x1, x2 to x2, y2 in Canvas
can_widget.create_line(0, 0, 800, 400)
can_widget.create_line(0, 400, 800, 0, fill="red")

# making a rectangle
can_widget.create_rectangle(50, 50, 700, 300, fill="blue")

# creating a text
can_widget.create_text(200, 200, text="Python Programme", fill="red")

# creating oval
can_widget.create_oval(140, 140, 260, 250)

root.mainloop()