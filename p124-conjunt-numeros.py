# p124-conjunto-numeros.py
#Crear y mostrar los conjuntos A, B y C a partir de las listas.

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

print("\n--- Operaciones de conjuntos ---")
print("Unión (A | B)                :", A | B)
print("Unión (B | C)                :", B | C)
print("Diferencia (A - C)           :", A - C)
print("Diferencia Simétrica (B ^ C)  :", B ^ C)
print("Intersección (B & C)         :", B & C)


print("\n--- Verificación de preguntas ---")


print(f"¿Es A subconjunto de B?          : {A.issubset(B)}")

print(f"¿Es C subconjunto de A?          : {C.issubset(A)}")

print(f"¿Está el número 100 en A?        : {100 in A}")

esta_en_todos = 60 in A and 60 in B and 60 in C
print(f"¿Está el número 60 en A, B y C?  : {esta_en_todos}")

print(f"¿No está el número 900 en C?     : {900 not in C}")