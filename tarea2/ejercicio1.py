
"""Crear una clase Gato que tenga 2 atributos, nombre y sonido. También agregar un método que permita saludar, 
en este método indicar que clase es a la que pertenece y cual es su sonido."""

class gato:

    def __init__(self, nombre, edad, maullido):
        self.nombre = nombre
        self.edad = edad
        self.maullido = maullido

    def __str__(self):
        return f"Me llamo {self.nombre} {self.maullido} acabo de cumplir {self.edad} años"

gato1 = gato("Nieve",8,"Miau")
print(gato1)

