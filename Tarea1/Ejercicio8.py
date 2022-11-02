
#Ejercicio 8: Crear un script que reciba una cantidad infinita de números hasta decir basta, luego que imprima la suma de los números ingresados.

lista =[]
print("Por favor ingrese numeros y para salir escriba basta")
while True:
    valor = input("Ingrese un valor: ")
    if valor == "basta":
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print("Dato Invalido")
            exit()
resultado = 0
for x in lista:
    resultado += x

print(resultado)  
