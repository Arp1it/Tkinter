from tkinter import *


def updatestudentfromuserdetail():
    with open("userdetail.txt", "a") as f:
        pass

    with open("userdetail.txt", "r+") as f:
        l = f.read().split("\n")
        # print(l)

    a = (f"Student name is {username.get()}".lower() in l and f"Student mobile no. is {usermobileno.get()}".lower() in l)

    print(a)

    if a == True:
        with open("userdetail.txt", "r") as e:
            reading = e.read()

        coin = reading.replace(f"Student name is {username.get()}\nStudent mobile no. is {usermobileno.get()}\nStudent house location is {userlocation.get()}\n\n".lower(), "") 

        with open("userdetail.txt", "w") as z:
            m = z.write(coin)

def delstudentfromuserdetail():
    pass

def getvalues():
    with open("userdetail.txt", "a") as f:
        pass

    with open("userdetail.txt", "r+") as f:
        l = f.read().lower().split("\n")
        # print(l)

    a = (f"Student name is {username.get()}".lower() in l and f"Student mobile no. is {usermobileno.get()}".lower() in l)

    # print(a)

    if a != True:
        with open("userdetail.txt", "a+") as f:
            f.write(f"Student name is {username.get()}\nStudent mobile no. is {usermobileno.get()}\nStudent house location is {userlocation.get()}\n\n".lower())

    else:
        print("It already exist")

root = Tk()
root.geometry("300x200")
root.minsize(300, 150)
root.maxsize(655, 333)

root.title("Making a dance class form")

name = Label(text="Name").grid()
mobileno = Label(text="MobileNo.").grid(row=1)
location = Label(text="Location").grid(row=2)

username = StringVar()
usermobileno = StringVar()
userlocation = StringVar()

nameentry = Entry(root, textvariable=username)
mobilenoentry = Entry(root, textvariable=usermobileno)
locationentry = Entry(root, textvariable=userlocation)

nameentry.grid(row=0, column=1)
mobilenoentry.grid(row=1, column=1)
locationentry.grid(row=2, column=1)

Button(text="Submit", command=getvalues).grid()
Button(text="Update", command=updatestudentfromuserdetail).grid(row=3, column=2)
Button(text="Reset", command=delstudentfromuserdetail).grid(row=3, column=1)

root.mainloop()