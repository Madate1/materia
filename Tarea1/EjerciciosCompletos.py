#Desde aqui a mas adelante estan todos los ejercicios con triple (") 
 
"""#Ejercicio 1: Multiplicar 2 números sin usar el símbolo de la multiplicación

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el primer numero: "))

resultado = 0

while num2 != 0:

    resultado = resultado + num1
    num2 = num2 - 1

print("El resultado es: ", resultado)
"""

"""#Ejercicio 2: Ingresar nombre y apellido e imprimirlo al revés.

nombre = input("Ingrese su Nombre:")
apellido = input("ingrese su Apellido:")

print(apellido, nombre)
"""

#Ejercicio 3: Crear un script que encuentre el elemento menor de una lista



"""#Ejercicio 4: Crear un script que imprima el volumen de una esfera por su radio 4/3 * pi * r ** 3

pi = 3.1415
r = int(input("Escribe el radio:"))
volumen = 4/3 * pi * r**3

print("El volumen de la esfera es:",volumen,"metros cubicos")
"""

"""#Ejercicio 5: Crear una script que indique si el usuario es mayor de edad.

edad = int(input("Ingrese su edad:"))

if edad < 18 and edad > 1:
    print("es menor a 18 años")
elif edad >= 18 and edad <= 50: 
  print("es mayor de 18 años")
elif edad >= 50 and edad <= 100:
  print("es de tercera edad")
else: 
  print("Esta es una edad falsa")
"""

"""#Ejercicio 6: Crear un script que permita calcular si un número es par o impar.

num = int(input("Ingresa el numero:"))
if num%2 == 0:
  print(num,"Este numero es par")
  
else:
  print(num,"Este numero es impar") 
"""

#Ejercicio 7: Crear un script que indique cuantas vocales tiene una palabra.

#Ejercicio 8: Crear un script que reciba una cantidad infinita de números hasta decir basta, luego que imprima la suma de los números ingresados.
   
"""#Ejercicio 9: El objetivo del ejercicio es crear un sistema de calificaciones, tomando en cuenta la siguiente información:
1. El usuario proporcionará un valor entre 0 y 10.
2. Si está entre 9 y 10: imprimir una A
3. Si está entre 8 y menor a 9: imprimir una B
4. Si está entre 7 y menor a 8: imprimir una C
5. Si está entre 6 y menor a 7: imprimir una D
6. Si está entre 0 y menor a 6: imprimir una F
7. Cualquier otro valor debe imprimir: Valor desconocido
nota = 0

if nota <= 9 and nota >= 10:
    print("Obtuvo una A")
elif nota >= 8 and nota <= 9:
  print("Obtuvo una B")
elif nota >= 7 and nota <= 8: 
  print("Obtuvo una C")
elif nota >= 6 and nota <= 7:
    print("Obtuvo una D")
elif nota >= 0 and nota <= 6:
    print("Obtuvo una F")
else:
    print("Valor desconocido")
"""

"""#Ejercicio 10: Imprimir números de 5 a 1 de manera descendente 

descedente = [1,2,3,4,5]

for descedente in num:
    print(descedente)
"""

"""#Ejercicio 11: Imprimir los números naturales del 0 al 10 utilizando un ciclo  

i = 0

while i <= 10:
  print(i) 
  i+= 1 """

"""#Ejercicio 12: Calcular el área y el perímetro de un Rectángulo,
Crear las variables
alto (int)
ancho (int)
Área: alto * ancho
Perímetro: alto + ancho
alto = int(input("Ingresar lo alto del rectangulo:"))
ancho = int(input("Ingresar el ancho del rectangulo:"))

print(("El area del rectangulo es:"), alto * ancho,"metros cuadrados")

print("El perimetro del rectangulo es:", 2*(alto) + 2*(ancho),"metros")
"""

"""#Ejercicio 13: Iterar un rango de 0 a 10 e imprimir sólo los números divisibles entre 3

for rango in range(0, 10, 3):
  print(rango)
"""

"""#Ejercicio 14: Presentar un string con el titulo y el autor de un libro

Libro = {
    "Autor":"Margaret Atwood",
    "Año de publicacion":"1985",
    "Titulo":"El cuento de la criada",
    "Pais del autor":"Canadiense",
    "Paginas del libro":"413 Paginas",
}

print(Libro)

print("El nombre del autor es", Libro["Autor"], "su libro se titula", Libro["Titulo"], "y se publico en el año", Libro["Año de publicacion"], "su nacionalidad es", Libro["Pais del autor"], "y para finalizar su libro cuenta con:", Libro["Paginas del libro"])
"""

"""#Ejercicio 15: Solicitar al usuario dos valores: numero1 (int), numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es: numeroMayor

num1 = input("Ingrese el Primer valor:")
num2 = input("Ingrese el Segundo valor:")
 
if num1 > num2:
    print(num1,"es mayor que",num2)
elif num1  < num2:
    print(num1,"es menor que",num2)
elif num1 == num2:
    print(num1,"es igual que", num2)
else:
    print("No se encuentra los datos")
"""

#Ejercicio 16: Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for:
tupla = (13, 1, 8, 3, 2, 5, 8)



#Ejercicio 17: Crear un script que encuentre la potencia de un número ingresado por el teclado.



#Ejercicio 18: Dado dos números enteros, encontrar la suma.



"""#Ejercicio 19: Dado un número de 5 dígitos, devolver el número en orden inverso.

numero = input("Ingresa un numero de 5 digitos:")
revertir = 0
valor = int(numero)

while valor > 0:
    residuo = valor % 10
    revertir = (revertir * 10) + residuo
    valor //= 10
print('El inverso del número ingresado es: ', revertir)
"""

"""#Ejercicio 20: Crear un script para saludar desde Python.

nombre= input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")

print("Bienvemido a este curso",nombre,apellido)
print("Es un placer tenerte aqui")
"""

