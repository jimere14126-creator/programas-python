# p104-lista-impares.py
# Leer un entero n. Llenar una lista con los primeros n números impares.


def procesar_impares():
    # 1. Leer n y generar la lista de los primeros n números impares
    try:
        n = int(input("Introduzca la cantidad de números impares (n): "))
    except ValueError:
        print("Error: Debe ingresar un número entero.")
        return

    impares = []
    numero = 1
    while len(impares) < n:
        impares.append(numero)
        numero += 2

    print("\n--- Generación de Lista ---")
    print(f"Lista de los primeros {n} números impares: {impares}")

    # 2. Calcular suma y promedio
    suma_total = sum(impares)
    promedio = suma_total / n if n > 0 else 0

    print("\n--- Cálculos ---")
    print(f"Suma de los números: {suma_total}")
    print(f"Promedio de los números: {promedio:.1f}")

    # 3. Números divisibles entre 3
    divisibles_3 = [num for num in impares if num % 3 == 0]
    suma_divisibles = sum(divisibles_3)

    print("\n--- Divisibles entre 3 ---")
    print(f"Números divisibles entre 3: {divisibles_3}")
    print(f"Suma de los números divisibles entre 3: {suma_divisibles}")

    # 4. Búsqueda
    print("\n--- Búsqueda ---")
    try:
        buscar = int(input("Introduzca elemento a buscar: "))
        if buscar in impares:
            posicion = impares.index(buscar)
            print(f"Result: El elemento {buscar} está en la lista en la posición (índice) {posicion}.")
        else:
            print(f"Result: El elemento {buscar} NO está en la lista.")
    except ValueError:
        print("Error: Ingrese un número válido para buscar.")

if __name__ == "__main__":
    procesar_impares()