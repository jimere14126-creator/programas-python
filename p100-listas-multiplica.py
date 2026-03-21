# p100-listas-multiplica.py
# Leer dos listas, cada una con 5 elementos numéricos. Crear una tercera lista multiplicando los elementos de las dos listas correspondientes. Imprimir las tres listas.

def multiplicar_listas():
    lista_a = []
    lista_b = []
    lista_c = []

    # Leer los 5 números para la Lista A
    print("Introduzca 5 números para la Lista A:")
    for i in range(5):
        num = float(input(f"Lista A - Elemento {i+1}: "))
        lista_a.append(num)

    # Leer los 5 números para la Lista B
    print("\nIntroduzca 5 números para la Lista B:")
    for i in range(5):
        num = float(input(f"Lista B - Elemento {i+1}: "))
        lista_b.append(num)

    # Calcular la Lista C multiplicando elementos correspondientes
    for i in range(5):
        resultado = lista_a[i] * lista_b[i]
        lista_c.append(resultado)

    # Imprimir los resultados
    print("\n--- Resultados ---")
    print(f"Lista A: {lista_a}")
    print(f"Lista B: {lista_b}")
    print(f"Lista C (A * B): {lista_c}")

if __name__ == "__main__":
    multiplicar_listas()