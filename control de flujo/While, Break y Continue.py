
i = 0

while i <= 10:
  print(i) #si se corre el while sin lo de abajo se ira hasta el infinito
  i = i + 1 #se puede cambiar por "i+=1


i = 1

while i <= 100: #Numeros par
    if i%2 == 0:
        print(i)
        i+=1
    elif i%2 ==1:
        i+=1 

i = 1 

while i <= 500: #Numeros impar
    if i%2 == 1:
        print(i)
        i+= 1
    elif i%2 == 0:
        i+= 1 
        

#Break
i = 0

while i < 10:
  print(i)
  if i == 3:
    break
  i+=1

#Continue
i = 0

while i < 10:
  i+=1 #se intercambia con print  <---
  if i == 3:
    continue
  print(i) # se invierten <--
