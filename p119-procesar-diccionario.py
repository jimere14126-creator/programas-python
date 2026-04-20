# p119-procesar-diccionario.py
# Crea un diccionario nomina combinando ambas listas (los nombres son las llaves, los sueldos son los valores).

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]


nomina = dict(zip(nombres, sueldos))


print("Diccionario de nómina:")
print(nomina)


print("\n--- Iterando Llaves (keys) ---")
for nombre in nomina.keys():
    print(nombre)

print("\n--- Iterando Valores (values) ---")
for sueldo in nomina.values():
    print(sueldo)

print("\n--- Iterando Llave y Valor (accediendo por llave) ---")
for nombre in nomina:
    print(f"{nombre} -> {nomina[nombre]}")

print("\n--- Iterando Llave y Valor (items) ---")
for item in nomina.items():
    print(item)

print("\n--- Cálculos ---")
suma_total = sum(nomina.values())
promedio = suma_total / len(nomina)

print(f"Suma total de sueldos: {suma_total:.2f}")
print(f"Promedio de sueldos: {promedio:.2f}")