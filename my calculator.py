from tkinter import *


class TEXT(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")

    def s(self):
        self.scvalue = StringVar()
        self.scvalue.set("")
        self.screen = Entry(textvariable=self.scvalue, font="lucida 40 bold")
        self.screen.pack(fill=X, ipadx=8, pady=10, padx=10)

    def click(self, event):
        text = event.widget.cget("text")
        # print(type(text))

        if text == "=":
            value = self.scvalue.get()

            if self.scvalue != self.scvalue.get().isdigit():
                try:
                    value = eval(self.screen.get())
                except Exception as e:
                    print(e)
                    value = "Error"

            self.scvalue.set(value)
            self.screen.update()

        elif text == "C":
            self.scvalue.set("")
            self.screen.update()

        else:
            self.scvalue.set(self.scvalue.get() + str(text))
            self.screen.update()

    def buttons(self, packi, text, font, side):
        self.b = Button(packi, text=text, font=font)
        self.b.pack(side=side, padx=25, pady=15)
        self.b.bind("<Button-1>", self.click)

if __name__=="__main__":
    gui = TEXT()
    gui.s()

    f = Frame()
    for i in range(9, 6, -1):
        gui.buttons(f, i , "lucida 20 bold", LEFT)
    f.pack()

    f = Frame()
    for i in range(6, 3, -1):
        gui.buttons(f, i, "lucida 20 bold", LEFT)
    f.pack()

    f = Frame()
    for i in range(3, 0, -1):
        gui.buttons(f, i, "lucida 20 bold", LEFT)
    f.pack()

    f = Frame()
    gui.buttons(f, "C", "lucida 20 bold", LEFT)
    gui.buttons(f, "0", "lucida 20 bold", LEFT)
    gui.buttons(f, ".", "lucida 20 bold", LEFT)
    f.pack()

    f = Frame()
    gui.buttons(f, "+", "lucida 20 bold", LEFT)
    gui.buttons(f, "-", "lucida 20 bold", LEFT)
    gui.buttons(f, "*", "lucida 20 bold", LEFT)
    f.pack()

    f = Frame()
    gui.buttons(f, "/", "lucida 20 bold", LEFT)
    gui.buttons(f, "%", "lucida 20 bold", LEFT)
    gui.buttons(f, "=", "lucida 20 bold", LEFT)
    f.pack()

    gui.mainloop()