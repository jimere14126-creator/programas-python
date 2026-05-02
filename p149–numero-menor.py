#p149–numero-menor.py
#Crea un programa que incluya una función. Dicha función debe solicitar 3 números enteros al usuario y devolver el menor.


def numero_menor():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    c = int(input("Introduce el tercer número: "))
    
    menor = min(a, b, c)
    return menor

# Programa principal
print("El número menor es:", numero_menor())