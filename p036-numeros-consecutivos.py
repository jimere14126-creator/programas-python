# p036-numeros-consecutivos.py
# Verificar si tres números son consecutivos

print('Dame 3 números enteros separados por espacio:')
n1, n2, n3 = input().split()

n1, n2, n3 = int(n1), int(n2), int(n3)

if (n2 == n1 + 1 and n3 == n2 + 1) or (n1 == n2 + 1 and n3 == n1 + 1) or (n1 == n3 + 1 and n2 == n1 + 1):
    print("Los números son consecutivos.")
else:
    print("Los números NO son consecutivos.")

print("\nPrograma terminado")