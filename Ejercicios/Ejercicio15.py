
#Ejercicio 15: Solicitar al usuario dos valores: numero1 (int), numero2 (int)
"""
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es: numeroMayor
"""
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
