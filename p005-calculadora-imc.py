# p005-calculadora-imc.py


print("calculadora de indice de masa corporal :")

peso_kg = float(input("dame tu peso en kilogramo:"))
altura_m = float(input("dame tu altura en metros:"))

imc = peso_kg / altura_m ** 2

print(f"si tienes un peso de {peso_kg} y una altura de {altura_m} tu imc es {imc:2f}")
