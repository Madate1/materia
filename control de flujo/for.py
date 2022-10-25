
vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    print(vocales)


#Ejemplo de for con break 

nombres =["Juan", "Pedro", "Maria", "Luis"]

for nombre in nombres:
    print(nombre)
    if nombre == "Pedro": #Se detiene la secuancia al llegar a este nombre
        break

#Ejemplo de for con continue

nombres =["Juan", "Pedro", "Maria", "Luis"]

for nombre in nombres:
    if nombre == "Pedro": #Se salta este nombre pero continua la secuencia
        continue
    print(nombre)
    