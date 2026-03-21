# p099-procesar-notas.py
# Leer un número indeterminado de notas (calificaciones) entre 0 y 100, deteniéndose cuando el usuario introduzca un 0.

def procesar_notas():
    notas = []
    
    print("Introduzca notas (entre 0 y 100). Introduzca 0 para detener.")
    
    while True:
        try:
            nota = float(input("Introduzca nota (0 para detener): "))
            
            if nota == 0:
                break
            
            if 0 < nota <= 100:
                notas.append(nota)
            else:
                print(" <- Entrada inválida, debe ser 0-100")
        except ValueError:
            print(" <- Por favor, ingrese un número válido.")

    if len(notas) == 0:
        print("\nNo se introdujeron notas.")
        return

    # Cálculos
    total_notas = len(notas)
    suma_notas = sum(notas)
    promedio = suma_notas / total_notas
    nota_max = max(notas)
    nota_min = min(notas)
    
    # Notas menores al promedio
    notas_menores = [n for n in notas if n < promedio]
    cantidad_menores = len(notas_menores)

    # Resultados
    print("\n--- Resultados ---")
    print(f"Total de notas introducidas: {total_notas}")
    print(f"Lista de notas: {notas}")
    print(f"Suma de notas: {suma_notas}")
    print(f"Promedio de notas: {promedio:.1f}")
    print(f"Nota máxima: {nota_max}")
    print(f"Nota mínima: {nota_min}")
    print(f"Notas menores al promedio ({promedio:.1f}): {cantidad_menores}")
    print(f"Lista de notas menores al promedio: {notas_menores}")

if __name__ == "__main__":
    procesar_notas()