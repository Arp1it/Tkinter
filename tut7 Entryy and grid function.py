from tkinter import *


def getvals():
    print(f"The username is {uservalue.get()}")
    print(f"The user password is {passvalue.get()}")

rooot = Tk()
rooot.geometry("655x333")
rooot.title("Using Grid")

user = Label(text="Username")
password = Label(text="Password")
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

# StringVar-
uservalue = StringVar()
# passvalue = IntVar()
passvalue = StringVar()

userentry = Entry(rooot, textvariable=uservalue)
passentry = Entry(rooot, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

rooot.mainloop()