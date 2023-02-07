from tkinter import *
from tkinter.messagebox import showinfo, askquestion
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


class Notepad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("655x555")

        self.textarea = Text(self, font="lucida 13")
        self.file = None
        self.textarea.pack(expand=True, fill=BOTH)

    def scrollbart(self):
        scroll = Scrollbar(self.textarea)
        scroll.pack(side=RIGHT, fill=Y)

        scroll.config(command=self.textarea.yview)
        self.textarea.config(yscrollcommand=scroll.set)

    def newfile(self):
        self.title("Untitled - Notepad")
        self.file = None
        self.textarea.delete(1.0, END)

    def openfile(self):
        self.file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text documents", "*.txt")])

        if self.file == "":
            self.file = None

        else:
            self.title(os.path.basename(self.file) + "- Notepad")
            self.textarea.delete(1.0, END)
            with open(self.file, "r") as f:
                self.textarea.insert(1.0, f.read())

    def savefile(self):

        if self.file == None:
            self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text documents", "*.txt")])

            if self.file == "":
                self.file = None

            else:
                self.title(os.path.basename(self.file) + "- Notepad")
                with open(self.file, "w") as f:
                    f.write(self.textarea.get(1.0, END))

        else:
            self.title(os.path.basename(self.file) + "- Notepad")
            with open(self.file, "w") as f:
                f.write(self.textarea.get(1.0, END))

    def Cut(self):
        self.textarea.event_generate(("<<Cut>>"))

    def Copy(self):
        self.textarea.event_generate(("<<Copy>>"))

    def Paste(self):
        self.textarea.event_generate(("<<Paste>>"))

    def Quit(self):
        h = askquestion("Save", "Save or not")
        print(type(h))
        if h == "yes":
            self.savefile()
            print("Thanks for using our notepad")

        if h == "no":
            print("Thanks for using our notepad")

        self.destroy()

    def help(self):
        showinfo("Notepad", "This Notepad is Design by Arpit")

    def menu1(self, g, b, c):
        a = [self.Cut, self.Copy, self.Paste]
        l = ["Cut", "Copy", "Paste"]

        j = [self.newfile, self.openfile, self.savefile, self.Quit]
        t = ["New File", "Open File", "Save File", "Exit"]

        q = [self.help]
        s = ["help"]

        Menubar = Menu(self)
        
        if g == True:
            Filemenu = Menu(Menubar, tearoff=0)

            for i, k in enumerate(j):
                if t[i] == "Exit":
                    Filemenu.add_separator()

                Filemenu.add_command(label=t[i], command=k)

            Menubar.add_cascade(label="File", menu=Filemenu)
        
        if b == True:
            Editmenu = Menu(Menubar, tearoff=0)

            for i, k in enumerate(a):
                Editmenu.add_command(label=l[i], command=k)

            Menubar.add_cascade(label="Edit", menu=Editmenu)

        if c == True:
            Help = Menu(Menubar, tearoff=0)

            for i, k in enumerate(q):
                Help.add_command(label=s[i], command=k)

            Menubar.add_cascade(label="About", menu=Help)

        self.config(menu=Menubar)

if __name__=="__main__":
    note = Notepad()

    note.menu1(True, True, True)
    note.scrollbart()

    note.mainloop()
