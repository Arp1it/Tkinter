from tkinter import *
from tkinter import ttk
import requests
from tqdm.tk import tqdm
from functools import partial

root = Tk()
root.geometry("600x500")
root.minsize(145, 50)
root.maxsize(900, 600)

frm = ttk.Frame(root)
frm.grid()

def down():
    # progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
    r = requests.get("https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-621.exe", stream=True)
    totalbyte = int(r.headers['Content-Length'])

    print(totalbyte)
    byte = 0

    progress_bar = tqdm(total=totalbyte, unit='B', unit_scale=True, tk_parent=root)

    with open("win.rar", "wb") as f:
        for chunk in r.iter_content(chunk_size=120):
            progress_bar.update(120)
            f.write(chunk)
            byte += 120
            root.update()

    progress_bar.close()
    progress_bar._tk_window.destroy()
    print(byte)

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Download win.rar file", command=partial(down)).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=0)

root.mainloop()