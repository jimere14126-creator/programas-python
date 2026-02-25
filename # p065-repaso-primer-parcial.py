# p065-repaso-primer-parcial.py
# Una papelería necesita un programa para gestionar eficientemente el control de sus ventas de fotocopias. El sistema debe ser capaz de registrar múltiples ventas, calcular los subtotales por tipo de copia y el total general. Además, deberá clasificar.


print("-" * 40)
print("Papelería la Malena, SA. de CV.")
print("Sistema de ventas de copias")
print("-" * 40)

# Inicialización de variables globales (totales del día)
cant_carta = 0; total_carta = 0
cant_oficio = 0; total_oficio = 0
cant_doble = 0;  total_doble = 0
cant_plano = 0;  total_plano = 0
ventas_realizadas = 0

otra_venta = "S"

# Ciclo principal de registro de ventas
while otra_venta == "S":
    ventas_realizadas += 1
    print(f"\nVenta: {ventas_realizadas}")
    
    # ENTRADA DE DATOS
    tipo = input("Tipo de copia (C)arta $3, (O)ficio $4, (D)oble Of $6, (P)lano $12 ? ").upper()
    cantidad = int(input("Cantidad ? "))
    
    # PROCESO: Determinar precio unitario
    precio = 0
    if tipo == "C":
        precio = 3
    elif tipo == "O":
        precio = 4
    elif tipo == "D":
        precio = 6
    elif tipo == "P":
        precio = 12
    else:
        print("Tipo de copia no válido.")
        continue

    subtotal = cantidad * precio
    
    # Lógica de Descuento por Volumen (Más de 50 unidades)
    if cantidad > 50:
        descuento = subtotal * 0.10
        subtotal -= descuento
        print(f"*** Descuento del 10% aplicado por volumen! ***")
    
    # Acumulación de totales según el tipo
    if tipo == "C":
        cant_carta += cantidad; total_carta += subtotal
    elif tipo == "O":
        cant_oficio += cantidad; total_oficio += subtotal
    elif tipo == "D":
        cant_doble += cantidad; total_doble += subtotal
    elif tipo == "P":
        cant_plano += cantidad; total_plano += subtotal

    otra_venta = input("Otra venta (S/N) ? ").upper()

# SALIDA: Resumen diario de ventas
total_final_dinero = total_carta + total_oficio + total_doble + total_plano
total_final_copias = cant_carta + cant_oficio + cant_doble + cant_plano

print("\n" + "-" * 40)
print("Resumen diario de ventas")
print("-" * 40)
print(f"Ventas realizadas: {ventas_realizadas}")
print("-" * 40)
print(f"Carta     : {cant_carta:3}  - $ {total_carta:8.2f}")
print(f"Oficio    : {cant_oficio:3}  - $ {total_oficio:8.2f}")
print(f"Doble Of. : {cant_doble:3}  - $ {total_doble:8.2f}")
print(f"Plano     : {cant_plano:3}  - $ {total_plano:8.2f}")
print("-" * 40)
print(f"Tot. Ventas : {total_final_copias:3}  - $ {total_final_dinero:8.2f}")

# Clasificación del desempeño del día
if total_final_dinero < 50:
    mensaje = "Venta moderada"
elif 50 <= total_final_dinero <= 150:
    mensaje = "Venta frecuente"
else:
    mensaje = "Venta superada"

print(f"Esta venta es una : {mensaje}")