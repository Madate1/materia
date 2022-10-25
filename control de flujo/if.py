 
if 2 != 2:
    print("2 es diferente a 2")
if 2 == 2:
    print("2 es igual a 2")
    
"""
Calcular la edad de una persona
Si es menor de 18 años imprimir "menor a 18 años"
Si es mayor de 18 años imprimir "mayor a 18 años"
Si es mayor de 50 años imprimir "mayor a 50 años"
"""
edad = 40

if edad < 18 and edad > 1: #AND solo se ejecuta si ambas condiciones son verdaderas.
    print("es menor a 18 años")
elif edad >= 50 and edad <= 100:
  print("es de tercera edad")
elif edad >= 18 and edad <= 50: 
  print("es mayor de 18 años")
else: 
  print("Esta es una edad falsa")

