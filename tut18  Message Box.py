from tkinter import *
import tkinter.messagebox as tmsg


def myfunc():
    print("Hey this is my menu")

def help():
    print("I will help you.")
    tmsg.showinfo("Help", "I will help you")

def rate_us():
    print("Please rate us")
    a = tmsg.askquestion("How was your experene", "Was your experience good")
    print(a)

    if a == "yes":
        title = "Rate us"
        msg = "Great. Rate us on appstore please."

    if a == "no":
        title = "Feedback us"
        msg = "I will help you please call on this number for feedbak 967XXXXX77"

    tmsg.showinfo(title, msg)

def Be_friend():
    ans = tmsg.askretrycancel("Dosti kara lo", "Sorry nahi banegi dost")
    print(ans)

    if ans:
        print("Retry karne pe sayad ho sakta")

    else:
        print("Bahut acha kiya padhai pe dyana lagega aba full marks ayenge")

root = Tk()
root.geometry("733x566")
root.title("Visual Studio Code")

mymanu = Menu(root)
m1 = Menu(mymanu, tearoff=0)
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Delete", command=myfunc)
m1.add_command(label="New Project", command=myfunc)
m1.add_separator()
m1.add_command(label="Print", command=myfunc)

mymanu.add_cascade(label="File", menu=m1)

m2 = Menu(mymanu)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)
m2.add_separator()
m2.add_command(label="Exit", command=quit)


mymanu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mymanu)
m3.add_command(label="help", command=help)
m3.add_command(label="Rate us", command=rate_us)
m3.add_command(label="Befriend Astha", command=Be_friend)

root.config(menu=mymanu)
mymanu.add_cascade(label="Help", menu=m3)

root.mainloop()