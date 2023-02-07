from tkinter import *


def click(event):
    global scvalue

    text = event.widget.cget("text")
    # print(type(text))

    if text == "=":
        value = scvalue.get()

        if scvalue != scvalue.get().isdigit():
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + str(text))
        screen.update()

root = Tk()

root.geometry("550x600")
root.title("My Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


f = Frame(root, background="white")
for i in range(9, 6, -1):
    b = Button(f, text=i, padx=5, pady=5, font="lucida 20 bold")
    b.pack(side = LEFT, padx=50, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, background="white")
for i in range(6, 3, -1):
    b = Button(f, text=i, padx=5, pady=5, font="lucida 20 bold")
    b.pack(side = LEFT, padx=50, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, background="white")
for i in range(3, 0, -1):
    b = Button(f, text=i, padx=5, pady=5, font="lucida 20 bold")
    b.pack(side = LEFT, padx=50, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, background="white")
b = Button(f, text="C", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, background="white")
b = Button(f, text="-", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, background="white")
b = Button(f, text="%", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=5, pady=5, font="lucida 20 bold")
b.pack(side = LEFT, padx=50, pady=10)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()