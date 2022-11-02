
primerNumero = int(input("Por favor ingrese el primer valor:"))

try:
    primero = int(primerNumero)
except:
    primero = "Cadena"

if primero == "Cadena":
    print("El valor ingresado no es un entero")
    exit()

segundoNumero = int (input("Por favor ingrese el segundo valor:"))
 
try:
    segundo = int(segundoNumero)
except:
    segundo = "Cadena"

if segundo == "Cadena":
    print("El valor ingresado no es un entero")
    exit()

"""suma = primerNumero + segundoNumero 
print("La suma de",primerNumero,"+",segundoNumero, "es =", suma)

resta = primerNumero - segundoNumero
print("La resta de",primerNumero,"-",segundoNumero, "es =", resta)

multiplicacion = primerNumero * segundoNumero
print("La Multiplicacion de",primerNumero,"x",segundoNumero, "es =", multiplicacion)

division = primerNumero / segundoNumero #Division
print("La Division de",primerNumero,"/",segundoNumero, "es =", division)"""

simbolo = input("Porfavor ingrese la el signo que desea usar: (+ - * /): ")

if simbolo == "+": 
    print(print("La suma de",primerNumero,"+",segundoNumero, "es =", primero + segundo))
elif simbolo == "-":
    print(print("La resta de",primerNumero,"-",segundoNumero, "es =", primero - segundo))
elif simbolo == "*":
    print(print("La multiplicacion de",primerNumero,"*",segundoNumero, "es =", primero * segundo))
elif simbolo == "/":
    print(print("La division de",primerNumero,"/",segundoNumero, "es =", primero / segundo))   
else:
    print("No es posible de calcular") 
