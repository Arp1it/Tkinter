from tkinter import *
import tkinter.messagebox as tmsg


def order():
    tmsg.showinfo("Your Order", f"Your {var.get()} order is reieved Successfully. Thanks for ordering!")

root = Tk()

root.geometry("455x233")
root.title(" ")

# var = IntVar()
# var.set(1)

var = StringVar()
var.set("Radio")

Label(root, text="What would you like to have sir?", font="lucida 15 bold", justify=LEFT, padx=14).pack()

l = ["Dosa", "Idaly", "Burger", "Samosa", "Mungorry"]
# for i, item in enumerate(l):
#     # print(item)
#     radio = Radiobutton(root, text=item, padx=14, pady=5, variable=var, value=i+1).pack(anchor="w")

for i in l:
    # print(item)
    radio = Radiobutton(root, text=i, padx=14, pady=5, variable=var, value=i).pack(anchor="w")

F = Frame(root, padx=15)
Button(F, text="ordered", padx=10, command=order).pack()
F.pack(anchor="e")

root.mainloop()