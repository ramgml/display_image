import tkinter as tk
from PIL import Image, ImageTk
from sys import argv


def main(image_path):
    root = tk.Tk()

    label = tk.Label(root)
    img = Image.open(image_path)
    label.img = ImageTk.PhotoImage(img)
    label['image'] = label.img

    label.pack()
    root.mainloop()


if __name__ == '__main__':
    main(argv[1])
