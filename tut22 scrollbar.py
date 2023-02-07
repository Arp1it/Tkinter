from tkinter import *


root = Tk()

root.title("My Scrollbar")
root.geometry("455x233")

# For connecting scrollbar to a widgit
# 1.widget(yscrollcommand = scrollbar.set)
# 2.scrollbar.config(command = widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill=Y)

# listbox = Listbox(root, yscrollcommand = scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f"item {i}")

# listbox.pack(fill="both", padx=22)
# scrollbar.config(command = listbox.yview)

text = Text(root, yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command = text.yview)

root.mainloop()