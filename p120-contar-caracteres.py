# p120-contar-caracteres.py
# Escribe un programa que pida al usuario que ingrese una cadena de texto.

cadena = input("Ingrese una cadena: ")

frecuencia = {}


for caracter in cadena:
    
    if caracter in frecuencia:
        
        frecuencia[caracter] += 1
    else:
      
        frecuencia[caracter] = 1

print("Resultado:")
print(frecuencia)