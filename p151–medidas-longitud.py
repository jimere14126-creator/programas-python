#p151–medidas-longitud.py
#Desarrolla un programa que funcione como un conversor de unidades de longitud.

def pulgadas_a_cm(pulgadas):
    return pulgadas * 2.54

def metros_a_pies(metros):
    return metros * 3.281

# Programa principal
while True:
    print("\n*** Conversor de Unidades ***")
    print("1. Pulgadas a centímetros")
    print("2. Metros a pies")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        pulgadas = float(input("Introduce pulgadas: "))
        print(pulgadas, "pulgadas =", pulgadas_a_cm(pulgadas), "cm")
    
    elif opcion == "2":
        metros = float(input("Introduce metros: "))
        print(metros, "metros =", metros_a_pies(metros), "pies")
    
    elif opcion == "3":
        break
    
    else:
        print("Opción inválida")