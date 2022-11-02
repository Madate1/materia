
#Ejercicio 1: Multiplicar 2 números sin usar el símbolo de la multiplicación

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el primer numero: "))

resultado = 0

while num2 != 0:

    resultado = resultado + num1
    num2 = num2 - 1

print("El resultado es: ", resultado)
