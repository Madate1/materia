
diccionario = {
    "nombre":"Mateo",
    "apellido":"Morocho",
    "edad":"19",
    "ciudad":"Cuenca",
}
print(type(diccionario))
print(diccionario)

print("La edad de", diccionario["nombre"], "es de", diccionario["edad"], "años y vive en", diccionario["ciudad"]) #Ejemplo de como aplicariamos el diccionario

print(len(diccionario)) #Solo cuenta los datos no la respuesta

#Recopilador de datos
perros = {
  "Tobby":{
    "name": "Tobby",
    "age": 6
    },
  "Leo":{
    "name": "Leo",
    "age": 1
    }
}
print(perros)

perritos = dict(name="Rocky", age=7) #Diferente forma de diccionario pero sirve igual
print(perritos)
