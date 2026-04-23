# p129-func-param-nombre.py

def saluda(apaterno: str, amaterno: str, nombre: str) -> None:
         print(f'Hola {nombre} {apaterno} {amaterno}')

saluda('Reyes', 'Avila', 'Jimena')
saluda(nombre='Jimena', amaterno='Avila', apaterno='Reyes')

