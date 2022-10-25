
#Ejercicio 5: Crear una script que indique si el usuario es mayor de edad.

edad = int(input("Ingrese su edad:"))

if edad < 18 and edad >= 1:
    print("es menor a 18 años")
elif edad >= 18 and edad <= 54: 
  print("es mayor de edad")
elif edad >= 55 and edad <= 100:
  print("es de tercera edad")
else: 
  print("Esta es una edad falsa")
