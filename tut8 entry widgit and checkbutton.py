from tkinter import *


def getvals():
    print("Submitting form")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}")

    with open("reords.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n")

root = Tk()

root.geometry("644x344")

# heading
Label(root, text="Welcome to harry travels", font="comicsansms 15 bold", pady=13).grid(row=0, column=5)

# textvalues nad pack it here
name = Label(root, text="Name").grid(row=1, column=2)
phone = Label(root, text="Phone").grid(row=2, column=2)
gender  = Label(root, text="Gender").grid(row=3, column=2)
emergency = Label(root, text="Emergency Contact").grid(row=4, column=2)
paymentmode = Label(root, text="Payment Mode").grid(row=5, column=2)

# tkinter variable for starting entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# packing entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# making a checkbox and packing it with the help of grid
foodservice = Checkbutton(text="Want to get your meals?", variable=foodservicevalue).grid(row=6, column=5)

# Button packing it and assignd a command
Button(text="Submit to harry travels", command=getvals).grid(row=10, column=7)

root.mainloop()