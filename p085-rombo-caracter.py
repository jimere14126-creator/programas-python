#p085-rombo-caracter.py
#Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo.


n = int(input("Dame un número impar para la altura: "))
caracter = input("¿Qué carácter quieres usar? ")

mitad = n // 2

# Parte superior del rombo
for i in range(mitad + 1):

    espacios = mitad - i
    estrellas = 2 * i + 1

    for j in range(espacios):
        print(" ", end="")

    for j in range(estrellas):
        print(caracter, end="")

    print()

# Parte inferior del rombo
for i in range(mitad - 1, -1, -1):

    espacios = mitad - i
    estrellas = 2 * i + 1

    for j in range(espacios):
        print(" ", end="")

    for j in range(estrellas):
        print(caracter, end="")

    print()