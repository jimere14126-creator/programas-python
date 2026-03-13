#p083-plan-ahorro-depistos-mensuales.py
#El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, un depósito mensual fijo, una tasa de interés mensual (porcentaje), y el número total de meses del plan.

saldo = float(input("Monto inicial de ahorro: "))
deposito = float(input("Depósito mensual: "))
tasa = float(input("Tasa de interés mensual (%): "))
meses = int(input("Número de meses a simular: "))

# Convertir porcentaje a decimal
tasa = tasa / 100

print("\n--- Plan de Ahorro Detallado ---")

# Ciclo para calcular cada mes
for mes in range(1, meses + 1):

    saldo_inicial = saldo

    # Calcular interés del mes
    interes = saldo_inicial * tasa

    # Calcular saldo final
    saldo = saldo_inicial + interes + deposito

    print("Mes", mes, "| Saldo Inicial: $", round(saldo_inicial,2),
          "| Interés: $", round(interes,2),
          "| Saldo Final: $", round(saldo,2))

print("\nAl final de", meses, "meses tendrás $", round(saldo,2))