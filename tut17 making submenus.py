from tkinter import *


def myfunc():
    print("Hey this is my menu")

root = Tk()
root.geometry("733x566")
root.title("Visual Studio Code")

# Use this to for creste non drop down menu
# mainmenu = Menu(root)
# mainmenu.add_command(label="File", command=myfunc)
# mainmenu.add_command(label="Exit", command=quit)
# root.config(menu=mainmenu)

mymanu = Menu(root)
m1 = Menu(mymanu, tearoff=0)
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Delete", command=myfunc)
m1.add_command(label="New Project", command=myfunc)
m1.add_separator()
m1.add_command(label="Print", command=myfunc)

# root.config(menu=mymanu)
mymanu.add_cascade(label="File", menu=m1)

m2 = Menu(mymanu)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)
m2.add_separator()
m2.add_command(label="Exit", command=quit)

root.config(menu=mymanu)
mymanu.add_cascade(label="Edit", menu=m2)

root.mainloop()