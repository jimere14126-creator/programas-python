# p004-paga-trabajador.py
# calcular la paga de un trabajador 


print("calcular la paga de un trabajador")

nombre = input("nombre >")
horas = int(input("horas trabajadas > "))
paga = float(input("paga x hora >"))

tasa = 0.3 
pagabruta = horas * paga 
impuesto = pagabruta * tasa 
paganeta = pagabruta - impuesto

print("resumen de pagos: \n")
print(f"el trabajador{nombre}, trabajo {horas}horas, con una paga de {paga} pesos, impuestos de {tasa} %")
print(f'Paga bruta {pagabruta}')
print(f'Impuesto {impuesto}')
print(f'Paga neta {paganeta}')