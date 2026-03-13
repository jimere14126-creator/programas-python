#p086-triangulo-invertido-numeros.py
#Solicitar al usuario un número entero n que determinará la altura de un triángulo numérico invertido.

n = int(input("Dame un número: "))

# Ciclo para cada fila
for i in range(n, 0, -1):

    # Imprimir números de 1 hasta i
    for j in range(1, i + 1):
        print(j, end=" ")

    print()  # salto de línea