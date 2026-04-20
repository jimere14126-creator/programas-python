# p123-conjunto-personas.py
# Crear y mostrar los conjuntos A (basado en la Lista 1) y B (basado en la Lista 2).

A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print("Conjunto A:", A)
print("Conjunto B:", B)

print("\n--- Operaciones de conjuntos ---")
print("Unión (A | B)           :", A | B)
print("Intersección (A & B)    :", A & B)
print("Diferencia (A - B)      :", A - B)
print("Diferencia Simétrica (A ^ B) :", A ^ B)


print("\n--- Verificación de afirmaciones ---")


afirmacion1 = {"Pablo", "Mateo"}.issubset(B)
print(f"¿Es {{'Pablo', 'Mateo'}} un subconjunto de B? : {afirmacion1}")


afirmacion2 = A.issuperset({"Reynaldo", "Angelica"})
print(f"¿Es A un superconjunto de {{'Reynaldo', 'Angelica'}}? : {afirmacion2}")

afirmacion3 = "Pedro" in A
print(f"¿Está 'Pedro' en el conjunto A? : {afirmacion3}")


afirmacion4 = "Lilia" not in B
print(f"¿No está 'Lilia' en el conjunto B? : {afirmacion4}")