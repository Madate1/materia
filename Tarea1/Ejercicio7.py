
#Ejercicio 7: Crear un script que indique cuantas vocales tiene una palabra.

frase = "El único modo de hacer un gran trabajo es amar lo que haces"
vocal = 0

for  x in frase:

    y = x.lower()
    if y == "a" or y == "e" or y == "i" or y == "o" or y == "u":
        vocal += 1

print("hay",vocal,"vocales")