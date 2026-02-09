# p009-promedio-de-calificaciones 
#objetivo: calcular el promedio de tres calificaciones ingresadas por el usuario 

print("calculando el primedio de tres calificaciones:\n")


#solicitar las calificaciones en una sola linea separadas por espacio 
print("Dame 3 calificaciones separadas por espacios:")
cal1, cal2, cal3 = input().split()
cal1, cal2, cal3 =  int(cal1), int(cal2), int(cal3)

#calcular el promedio 
promedio = (cal1 + cal2 + cal3)/3

## Mostrar el resultado incluyendo las calificaciones
print(f'Las calificaciones son: {cal1}, {cal2}, {cal3}')
print(f'El promedio de las calificaciones es: {promedio}')
