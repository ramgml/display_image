import tkinter as tk
from PIL import Image, ImageTk
from sys import argv
from time import sleep


def main(image_path, delay=5):
    root = tk.Tk()

    label = tk.Label(root)
    img = Image.open(image_path)
    label.img = ImageTk.PhotoImage(img)
    label['image'] = label.img

    label.pack()
    root.update()
    sleep(int(delay))
    root.destroy()


if __name__ == '__main__':
    main(*argv[1:3])
