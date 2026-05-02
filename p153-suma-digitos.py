#p153-suma-digitos.py
#Escribe un programa que procese una lista de números.
def leer_lista():
    numeros = list(map(int, input("Dame números separados por espacio: ").split()))
    return numeros

def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

def procesar_lista(lista):
    nueva = []
    for num in lista:
        nueva.append(suma_digitos(num))
    return nueva

# Programa principal
lista = leer_lista()
nueva_lista = procesar_lista(lista)

print("Lista original:", lista)
print("Lista con suma de dígitos:", nueva_lista)