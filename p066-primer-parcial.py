"""
Objetivo: El programa debe controlar la venta de boletos, gestionar el aforo y calcular los ingresos generados.
Nombre del Alumno: [Jimena Estefania Reyes Avila]
Matrícula: [20202177]
Materia: Computación Aplicada
Examen: Primer Parcial
"""

#Inicialización de Contadores y Acumuladores 
print("\033[H\033[J")
ventas = 0

#Contadores de Asistentes 
total_estudiantes = 0
total_adultos = 0
total_terceraedad = 0
total_academicos = 0
total_asistentes = 0
total_rechazados = 0
total_hombres = 0
total_mujeres = 0
suma_edades = 0

#Acumuladores de Ingresos
ingresos_estudiantes = 0.0
ingresos_adultos = 0.0
ingresos_terceraedad = 0.0
ingresos_academicos = 0.0
ingresos_totales = 0.0

#Precios de los Boletos (constantes) 
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCERAEDAD = 60.0
PRECIO_ACADEMICO = 70.0

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

#Ciclo Principal
continuar_venta = "s"
while continuar_venta == "s":
    ventas += 1
    print(f"\n Nueva Venta {ventas} ")

    edad = int(input("Introduce la edad del comprador: "))

    if edad <= 13:
        print(" Acceso denegado : El comprador es menor de edad")
        total_rechazados += 1
        continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()
        continue

    print('------------------------')
    print("\nTipo de comprador:")
    print("E Estudiante ($50)") 
    print("A Adulto ($90)")
    print("TER Tercera Edad ($60)")
    print("AC Académico ($70)")
    tipo_comprador = input("Elige el tipo de comprador (E/A/TE/AC): ").upper()
    print('--------------------------')
    sexo = input("Introduce el sexo del comprador (H/M): ").lower()
    print('--------------------------')

    if tipo_comprador == "E":
        tipo_texto = "Estudiante"
    elif tipo_comprador == "A":
        tipo_texto = "Adulto"
    elif tipo_comprador == "TER":
        tipo_texto = "Tercera Edad"
    elif tipo_comprador == "AC":
        tipo_texto = "Académico"
    else:
        print("Tipo de comprador no válido, venta cancelada")
        continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()
        continue

    print(f"¡Bienvenido(a)! Datos registrados: {edad} años, sexo: {'hombre' if sexo == 'h' else 'mujer'}, Tipo: {tipo_texto}")

    total_asistentes += 1
    suma_edades += edad
    if sexo == "h":
        total_hombres += 1
    elif sexo == "m":
        total_mujeres += 1

    if tipo_comprador == 'E':
        total_estudiantes += 1
        ingresos_estudiantes += PRECIO_ESTUDIANTE
        ingresos_totales += PRECIO_ESTUDIANTE
    elif tipo_comprador == 'A':
        total_adultos += 1
        ingresos_adultos += PRECIO_ADULTO
        ingresos_totales += PRECIO_ADULTO
    elif tipo_comprador == 'TER':
        total_terceraedad += 1
        ingresos_terceraedad += PRECIO_TERCERAEDAD
        ingresos_totales += PRECIO_TERCERAEDAD
    elif tipo_comprador == 'AC':
        total_academicos += 1
        ingresos_academicos += PRECIO_ACADEMICO
        ingresos_totales += PRECIO_ACADEMICO

    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- Cálculo de Promedio ---
promedio_edad = suma_edades / total_asistentes if total_asistentes > 0 else 0

# --- Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
print(f"Total Estudiantes: {total_estudiantes}")
print(f"Total Adultos: {total_adultos}")
print(f"Total Tercera Edad: {total_terceraedad}")
print(f"Total Académicos: {total_academicos}")
print('----------------------------------')
print(f"Total Hombres: {total_hombres}")
print(f"Total Mujeres: {total_mujeres}")
print('----------------------------------')
print(f"Total Asistentes: {total_asistentes}")
print(f"Promedio de edad: {promedio_edad:.2f}")
print(f"Total Rechazados (menores de 13 años): {total_rechazados}")

print("\n--- Reporte de Ingresos ---")
print(f"Ingresos Estudiantes: ${ingresos_estudiantes:.2f}")
print(f"Ingresos Adultos: ${ingresos_adultos:.2f}")
print(f"Ingresos Tercera Edad: ${ingresos_terceraedad:.2f}")
print(f"Ingresos Académicos: ${ingresos_academicos:.2f}")
print('----------------------------------')
print(f"TOTAL RECAUDADO: ${ingresos_totales:.2f}")

print("\n--- Rentabilidad ---")
if ingresos_totales < 1500:
    print("La función generó BAJAS ganancias.")
elif ingresos_totales <= 3500:
    print("La función generó ganancias MODERADAS.")
else:
    print("La función generó BUENAS ganancias.")

print("\nProceso terminado ✔")

"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.


-Le agregaria una pregunta al usuario para ver que dia de la semana es y le pondria la pregunta dia = input("¿Qué día es hoy? (Lu/Mar/Mier/Ju/Vi/Sa/Do): ").upper()
despues, en la parte donde se calcula el precio de los boletos de Adulto, pondria  una condición que seria:

Si el día es martes (Mar), aplico el descuento del 20% al precio del boleto de Adulto.

En caso contrario, mantengo el precio normal.
De esta forma, la lógica del descuento se integra directamente en la parte del código que calcula el costo del boleto.

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

-Primero analizaria cada bloque if y elif donde se calcula el precio del boleto, verificando que en todos los casos se esté sumando correctamente al acumulador general donde la instrucción sea: ingresos_totales += PRECIO_....
Si en alguno de esos bloques falta esa línea, el total no se actualizaría correctamente.
También comprobaría que no haya instrucciones que resten o que cancelen la venta después de sumar ingresos.
Como paso adicional, imprimiría valores intermedios de ingresos_totales después de cada venta para confirmar que se está acumulando bien.
Las líneas críticas a revisar son las que actualizan los ingresos por tipo de comprador y la suma al total general.
"""
