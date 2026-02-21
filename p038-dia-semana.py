# p038-dia-semana.py
# Programa que muestra el día de la semana según un número del 1 al 7

# Solicitar número al usuario
numero = int(input("Ingresa un número del 1 al 7: "))


if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Lunes")
elif numero == 3:
    print("Martes")
elif numero == 4:
    print("Miércoles")
elif numero == 5:
    print("Jueves")
elif numero == 6:
    print("Viernes")
elif numero == 7:
    print("Sábado")
else:
    print("Error: Día inválido.")

print("\nPrograma terminado")