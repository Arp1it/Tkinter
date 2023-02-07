from tkinter import *
from PIL import ImageTk, Image


def ever_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i%100 == 0 and i!=0:
            final_text += "\n"
    return final_text

root = Tk()

root.geometry("1000x700")
root.title("My GUI")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(ever_100(text))

    image = Image.open(f"{i+1}.png")
    # TODO: Resize these image
    if i == 1:
        image = image.resize((195, 155), Image.ANTIALIAS)

    else:
        image = image.resize((125, 155), Image.ANTIALIAS)

    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=70)
Label(f0, text="Arpit's News", font="lucida 33 bold").pack()
Label(f0, text="August 26 2050", font="lucida 10 bold").pack()
f0.pack()

for k in range(0, 3):
    f1 =Frame(root, width=900, height=200)
    if k == 1:
        Label(f1, text=texts[k], padx=22, pady=25).pack(side="right")

    else:
        Label(f1, text=texts[k], padx=22, pady=25).pack(side="left")

    Label(f1, image=photos[k], anchor="e", padx=22, pady=35).pack()
    f1.pack()

root.mainloop()