from tkinter import *

root = Tk()
root.title("Abacom")
root.geometry("600x400")
#ctrol + f5 para correr el codigo
label0 = Label(root, text="Soy el label numero 0")
label1 = Label(root, text="Soy el lavel numero 1")
label2 = Label(root, text="Soy el label numero 2")
label3 = Label(root, text="Soy el label numero 3")


label0.grid(row=4, column=4)
label2.grid(row=10, column=10)  
label1.grid(row=6, column=6)
label3.grid(row=1, column=1)


root.mainloop()

