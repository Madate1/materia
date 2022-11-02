
"""Crear una clase Perro con los mismos métodos y atributos del Gato, la particularidad es que este debe 
indicar en el método saludo, que es un perro y su sonido."""

class perro:

    def __init__(self, nombre, edad, ladrido):
        self.nombre = nombre
        self.edad = edad
        self.ladrido = ladrido

    def __str__(self):
        return f"Me llamo {self.nombre} {self.ladrido} acabo de cumplir {self.edad} años"

perro1 = perro("Steven",4,"woof")
print(perro1)

