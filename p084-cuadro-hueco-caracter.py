#p084-cuadro-hueco-caracter.py
#El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujará.



lado = int(input("¿De qué tamaño será el lado del cuadrado? "))
caracter = input("¿Qué carácter quieres usar? ")

for i in range(lado):

    for j in range(lado):

        # Imprimir borde
        if i == 0 or i == lado-1 or j == 0 or j == lado-1:
            print(caracter, end=" ")
        else:
            print(" ", end=" ")

    print()  