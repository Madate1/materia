
#Ejercicio 19: Dado un número de 5 dígitos, devolver el número en orden inverso.

numero = input("Ingresa un numero de 5 digitos:")
revertir = 0
valor = int(numero)

while valor > 0:
    residuo = valor % 10
    revertir = (revertir * 10) + residuo
    valor //= 10 
print("El inverso del número ingresado es:",revertir)

