#p155-estadisticas-basicas.py
#Crea un programa que calcule estadísticas básicas (poblacionales) para una lista de números.

import math

def leer_lista():
    return list(map(int, input("Dame números separados por espacio: ").split()))

def mayor(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def media(lista):
    return sum(lista) / len(lista)

def varianza(lista):
    m = media(lista)
    return sum((x - m) ** 2 for x in lista) / len(lista)

def desviacion(lista):
    return math.sqrt(varianza(lista))

# Programa principal
lista = leer_lista()

print("\nEstadísticas:")
print("Mayor:", mayor(lista))
print("Menor:", menor(lista))
print("Media:", media(lista))
print("Varianza:", varianza(lista))
print("Desviación estándar:", desviacion(lista))