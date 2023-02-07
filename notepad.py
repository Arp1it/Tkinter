from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file

    root.title("Untitled - Notepad")
    file = None

    teaxtarea.delete(1.0, END)

def openFile():
    global file

    file=askopenfilename(defaultextension = ".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None

    else:
        root.title(os.path.basename(file) + "- Notepad")
        teaxtarea.delete(1.0, END)
        f = open(file, "r")
        teaxtarea.insert(1.0, f.read())
        f.close()

def saving():
    global file

    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(teaxtarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(teaxtarea.get(1.0, END))
        f.close()

def cut():
    teaxtarea.event_generate(("<<Cut>>"))

def copy():
    teaxtarea.event_generate(("<<Copy>>"))

def paste():
    teaxtarea.event_generate(("<<Paste>>"))

def help():
    showinfo("Notepad", "Arpit will help you - Notepad")

if __name__=="__main__":
    #Basic tkintesetup
    root = Tk()

    root.geometry("644x555")
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("5.ico")

    # Add text area
    teaxtarea = Text(root, font="lucida 13")
    file = None
    teaxtarea.pack(expand = True, fill=BOTH)

    # Create a menu bar
    Menubar = Menu()
    # File Menu Starts
    filemenu = Menu(Menubar, tearoff=0)
    # to open new file
    filemenu.add_command(label="New", command=newfile)
    
    # to open already existing file
    filemenu.add_command(label="Open", command=openFile)

    # to save the current file
    filemenu.add_command(label="Save", command=saving)

    filemenu.add_separator()

    # for exixiting the programme
    filemenu.add_command(label="Exit", command=root.destroy)
    Menubar.add_cascade(label="File", menu=filemenu)
    # File Menu Ends

    # Edit Menu Starts
    editmenu = Menu(Menubar, tearoff=0)

    # to give a feature of cut, copy and paste
    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)

    Menubar.add_cascade(label="Edit", menu=editmenu)
    # Edit Menu Ends

    # help Menu Starts
    helpmenu = Menu(Menubar, tearoff=0)

    helpmenu.add_command(label="Help", command=help)
    Menubar.add_cascade(label="About", menu=helpmenu)
    # help Menu Ends

    root.config(menu=Menubar)

    # Add scrollbar
    scroll = Scrollbar(teaxtarea)
    scroll.pack(side = RIGHT, fill=Y)

    scroll.config(command=teaxtarea.yview)
    teaxtarea.config(yscrollcommand=scroll.set)

    root.mainloop()