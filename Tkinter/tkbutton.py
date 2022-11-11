from tkinter import *

root = Tk()
root.title("Hola mundo")
root.geometry ("600x400")

def click():
    label = Label(root, text="Click aqui")
    label.pack()

btn = Button(root, text="click", command=click)
btn.pack()

root.mainloop()