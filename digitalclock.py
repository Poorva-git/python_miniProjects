from tkinter import *
import time

root = Tk()
root.title("Digital Clock")

label = Label(root, font=("Arial", 40), fg="blue")
label.pack()


def clock():
    current = time.strftime("%H:%M:%S")
    label.config(text=current)
    label.after(1000, clock)

clock()

root.mainloop()