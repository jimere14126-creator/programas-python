#p092-lista-de-gastos.py
# Desarrolla una aplicación que almacene gastos en una lista y permita al usuario manipularla a través de un menú que se mostrará continuamente hasta que decida salir.

gastos = []

while True:
    print("\n Menu de Control de Gastos")
    print("1. Ver Gastos")
    print("2. Agregar Gasto")
    print("3. Modificar Gasto")
    print("4. Eliminar Gasto")
    print("5. Ver Total de Gastos")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if len(gastos) == 0:
            print("No hay gastos registrados.")
        else:
            print("\nLista de gastos:")
            for i, gasto in enumerate(gastos):
                print(f"{i}: ${gasto}")

    elif opcion == "2":
        try:
            monto = float(input("Ingrese el monto del gasto: "))
            gastos.append(monto)
            print("Gasto agregado correctamente.")
        except:
            print("Error: Debe ingresar un número válido.")

    elif opcion == "3":
        try:
            indice = int(input("Ingrese el índice del gasto a modificar: "))
            if 0 <= indice < len(gastos):
                nuevo = float(input("Ingrese el nuevo monto: "))
                gastos[indice] = nuevo
                print("Gasto modificado correctamente.")
            else:
                print("Gasto no encontrado.")
        except:
            print("Error: Entrada inválida.")

    elif opcion == "4":
        try:
            indice = int(input("Ingrese el índice del gasto a eliminar: "))
            if 0 <= indice < len(gastos):
                gastos.pop(indice)
                print("Gasto eliminado correctamente.")
            else:
                print("Gasto no encontrado.")
        except:
            print("Error: Entrada inválida.")

    elif opcion == "5":
        total = sum(gastos)
        print(f"El total de gastos es: ${total}")

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")