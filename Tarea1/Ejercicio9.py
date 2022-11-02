#Ejercicio 9: El objetivo del ejercicio es crear un sistema de calificaciones, tomando en cuenta la siguiente información:
"""
1. El usuario proporcionará un valor entre 0 y 10.
2. Si está entre 9 y 10: imprimir una A
3. Si está entre 8 y menor a 9: imprimir una B
4. Si está entre 7 y menor a 8: imprimir una C
5. Si está entre 6 y menor a 7: imprimir una D
6. Si está entre 0 y menor a 6: imprimir una F
7. Cualquier otro valor debe imprimir: Valor desconocido
"""
nota = 7

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