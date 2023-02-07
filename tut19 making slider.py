from tkinter import *
import tkinter.messagebox as tmsg


def getdollar():
    tmsg.showinfo("Get Dollar", f"You withdraw {myslider2.get()} dollar Sucessfully on your Bank Account.")

root = Tk()

root.geometry("455x233")
root.title("Slider GUI")

# myslider = Scale(root, from_=0, to=455)
# myslider.pack()
Label(root, text="How many dollar you want?").pack()

myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.set(10)
myslider2.pack()

F1 = Frame(root, width=10, height=1, pady=10)
Button(F1, text="Get Dollars!", pady=5, command=getdollar).pack()
F1.pack()

root.mainloop()