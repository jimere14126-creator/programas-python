# p101-mes-dia-nombre.py
# Leer un número de mes (ej. 4). Guardar los días de cada mes en una lista y los nombres de los meses en otra lista. Asumir 28 días para febrero.

def mostrar_mes():
    # Listas predefinidas
    nombres = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    try:
        # Leer el número de mes
        numero_mes = int(input("Introduzca un número de mes (1-12): "))

        # Validar que el número esté en el rango correcto
        if 1 <= numero_mes <= 12:
            # El índice es numero_mes - 1 porque las listas empiezan en 0
            indice = numero_mes - 1
            
            print("\n--- Resultados ---")
            print(f"Mes: {nombres[indice]}")
            print(f"Días: {dias[indice]}")
        else:
            print("Error: El número debe estar entre 1 y 12.")
            
    except ValueError:
        print("Error: Por favor, introduzca un número entero válido.")

if __name__ == "__main__":
    mostrar_mes()