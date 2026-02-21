# p039-numeros-romanos.py
# Convertir un número entero a número romano

print("Dame un numero entero entre 1 y 10:")

num = int(input())

if num == 1:
    print(f"El numero {num} equivale a I en numero romano")
elif num == 2:
    print(f"El numero {num} equivale a II en numero romano")
elif num == 3:
    print(f"El numero {num} equivale a III en numero romano")
elif num == 4:
    print(f"El numero {num} equivale a IV en numero romano")
elif num == 5:
    print(f"El numero {num} equivale a V en numero romano")
elif num == 6:
    print(f"El numero {num} equivale a VI en numero romano")
elif num == 7:
    print(f"El numero {num} equivale a VII en numero romano")
elif num == 8:
    print(f"El numero {num} equivale a VIII en numero romano")
elif num == 9:
    print(f"El numero {num} equivale a IX en numero romano")
elif num == 10:
    print(f"El numero {num} equivale a X en numero romano")
else:
    print("Error: el numero debe estar entre 1 y 10.")

print("\n Programa terminado")