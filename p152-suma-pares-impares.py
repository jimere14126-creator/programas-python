#p152-suma-pares-impares.py
#Crea un programa que sume números pares o impares dentro de un rango especificado.

def suma_rango(inicio, fin, tipo):
    suma = 0
    
    for i in range(inicio, fin + 1):
        if tipo == "P" and i % 2 == 0:
            suma += i
        elif tipo == "I" and i % 2 != 0:
            suma += i
    
    return suma

# Programa principal
inicio = int(input("Introduce el número inicial: "))
fin = int(input("Introduce el número final: "))
tipo = input("¿Qué deseas sumar? (P)ares o (I)mpares: ").upper()

resultado = suma_rango(inicio, fin, tipo)
print("Resultado:", resultado)