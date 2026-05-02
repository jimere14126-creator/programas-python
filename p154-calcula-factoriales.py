#p154-calcula-factoriales.py
#Desarrolla un programa que calcule el factorial de cada número en una lista.

def leer_lista():
    return list(map(int, input("Dame números separados por espacio: ").split()))

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def lista_factoriales(lista):
    return [factorial(num) for num in lista]

# Programa principal
lista = leer_lista()
fact = lista_factoriales(lista)

print("Lista original:", lista)
print("Lista con factoriales:", fact)