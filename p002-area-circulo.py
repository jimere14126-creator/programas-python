# p002-area-circulo.py
# calcular area de un circulo 

import math #importar el modulo de funciones matematicas 
print("calcular el area de un circulo \n\n") #\n inserta una linea en blanco 
print("dame el radio:")

radio = float(input())
area = math.pi * math.pow(radio, 2)

print(f"el circulo de radio {radio:.2f} tiene un area de {area:.2f}")
