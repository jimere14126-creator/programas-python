#p150-dia-semana.py
#Escribe un programa con una función que reciba un número entero entre 1 y 7.

def dia_semana(num):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    
    if num in dias:
        return dias[num]
    else:
        return "Error: El número debe estar entre 1 y 7."

# Programa principal
numero = int(input("Introduce un número del 1 al 7: "))
print("El día es:", dia_semana(numero))