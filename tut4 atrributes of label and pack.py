from tkinter import *

root = Tk()
root.geometry("744x433")
root.title("MY TKINTER")

# important label options-
# text = adds the text
# bd - background
# fg - foreground
# font = sets the font - 1.font=("comicsansms", 10, "bold", "italic"), 2.font="comicsansms 10 bold italic"
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

t_label = Label(text='''The universe (Latin: universus) is all of space and time[a] and their contents,[10] \nincluding planets, stars, galaxies, and all other forms of matter and energy. The Big Bang theory is the \nprevailing cosmological description of the development of the universe. According to this theory, space and \ntime emerged together 13.787±0.020 billion years ago,[11] and the universe has been expanding ever since the \nBig Bang. While the spatial size of the entire universe is unknown,[3] it is possible to measure the size of \nthe observable universe, which is approximately 93 billion light-years in diameter at the present day.''', bg="black", fg="white", padx=23, pady=25, font="comicsansms 10 bold italic", borderwidth=20, relief=SUNKEN)

# Important Pack option-
# anchor = nw, ne - ex - (anchor="sw")
# side = top, bottom, left, right
# fill - (fill=X), (fill=Y)
# padx
# pady

t_label.pack(side = LEFT, anchor="sw", fill = Y, padx=34, pady=34)

root.mainloop()