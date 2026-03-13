#p082-compara-rendimiento-inversion.py
#Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años.

# Programa que compara el rendimiento de dos fondos de inversión

print("---Fondo de Inversión A--- ")
montoA = float(input("Monto inicial: "))
tasaA = float(input("Tasa de interés anual (%): "))

print("\n---Fondo de Inversión B---")
montoB = float(input("Monto inicial: "))
tasaB = float(input("Tasa de interés anual (%): "))

anios = int(input("\nAños a proyectar: "))

# Convertir porcentajes a decimal
tasaA = tasaA / 100
tasaB = tasaB / 100

print("\n ---Comparación de Rendimientos Anuales--- ")
print("Año | Fondo A | Fondo B")

# Ciclo para calcular cada año
for i in range(1, anios + 1):

    montoA = montoA + (montoA * tasaA)
    montoB = montoB + (montoB * tasaB)

    print(i, "| $", round(montoA,2), "| $", round(montoB,2))

# Comparación final
if montoA > montoB:
    print("\nResultado final: El Fondo A ($", round(montoA,2), ") superó al Fondo B ($", round(montoB,2), ").")
else:
    print("\nResultado final: El Fondo B ($", round(montoB,2), ") superó al Fondo A ($", round(montoA,2), ").")