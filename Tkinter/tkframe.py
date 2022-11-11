from tkinter import *

root = Tk()
root.title("Abacom")
root.geometry("600x400")

frame = LabelFrame(root, text="Login")
frame.pack()

label = Label (frame, text="Es un frame")
btn = Button(frame, text="salir", command=root.quit)

label.pack()
btn.pack()

root.mainloop()