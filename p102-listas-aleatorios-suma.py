# p102-listas-aleatorios-suma.py
# Generar 2 listas de 10 números aleatorios cada una. Crear una tercera lista donde el elemento sea la suma de los correspondientes de las listas A y B, solo si AMBOS elementos son impares.

import random

def procesar_aleatorios():
    # Generar 2 listas de 10 números aleatorios (rango 1 a 20 para el ejemplo)
    lista_a = [random.randint(1, 20) for _ in range(10)]
    lista_b = [random.randint(1, 20) for _ in range(10)]
    lista_c = []

    # Calcular la Lista C con la condición de impares
    for i in range(10):
        # Un número es impar si el residuo de dividirlo entre 2 no es 0
        if lista_a[i] % 2 != 0 and lista_b[i] % 2 != 0:
            suma = lista_a[i] + lista_b[i]
            lista_c.append(suma)
        else:
            lista_c.append(0)

    # Imprimir las listas generadas
    print("--- Listas Generadas ---")
    print(f"Lista A: {lista_a}")
    print(f"Lista B: {lista_b}")

    # Imprimir los resultados
    print("\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---")
    print(f"Lista C: {lista_c}")
    print("\nExplicación rápida:")
    print("Si ambos son impares -> se suman.")
    print("Si al menos uno es par -> el resultado es 0.")

if __name__ == "__main__":
    procesar_aleatorios()