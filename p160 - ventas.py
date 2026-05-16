#p160 - ventas.py

import os

class Prestamo:
    def __init__(self, libro, dias, tarifa_diaria):
        self.libro = libro
        self.dias = dias
        self.tarifa_diaria = tarifa_diaria
        self.total = dias * tarifa_diaria

    def __str__(self):
        return f"-> Libro: {self.libro:<22} Dias: {self.dias:>3}  Tarifa/Día: $ {self.tarifa_diaria:>6.2f}  Total: $ {self.total:>8.2f}"


class Usuario:
    def __init__(self, id_usuario, nombre, correo, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.prestamos = []

    def agregarPrestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def totalTarifas(self):
        total = 0
        for p in self.prestamos:
            total += p.total
        return total

    def __str__(self):
        return f"Usuario -> [Nombre: {self.nombre:<15} ID: {self.id_usuario:<12} Correo: {self.correo:<25} Tel: {self.telefono:<12} ]"


class Biblioteca:
    def __init__(self, nombre, domicilio, encargado):
        self.nombre = nombre
        self.domicilio = domicilio
        self.encargado = encargado
        self.usuarios = []

    def agregarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def totalPrestamos(self):
        total_libros = 0
        for u in self.usuarios:
            total_libros += len(u.prestamos)
        return total_libros

    def totalImportePrestamos(self):
        total_dinero = 0
        for u in self.usuarios:
            total_dinero += u.totalTarifas()
        return total_dinero

    def __str__(self):
        header = "=" * 115
        info = f"REPORTE DE CONTROL DE PRÉSTAMOS: Biblioteca -> [Nombre: {self.nombre}  Domicilio: {self.domicilio}\nEncargado: {self.encargado}]"
        return f"{header}\n{info}\n{header}"


def main():
    # Limpiar pantalla según el sistema operativo
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print('Inicio del programa en la función main() principal:\n')

    # Crear Biblioteca
    mi_biblio = Biblioteca('Biblioteca Mauricio Magdaleno', 'Calle Grillo 100, Col. Centro', 'Dra. Leticia Ramírez')

    # Crear Usuarios
    u1 = Usuario('USR-2026-X', 'Salvador Novo', 'snovo@cultura.gob.mx', '4921112233')
    u2 = Usuario('USR-2026-Y', 'Amparo Dávila', 'amparo@unam.mx', '4922223344')
    u3 = Usuario('USR-2026-Z', 'Juan Rulfo', 'jrulfo@literatura.mx', '4923334455')
    u4 = Usuario('USR-2026-W', 'Elena Garro', 'egarro@escritores.org', '4924445566')

    
    u1.agregarPrestamo(Prestamo('Laberinto de la Soledad', 6, 11.50))
    u1.agregarPrestamo(Prestamo('Pedro Páramo', 4, 14.00))

    u2.agregarPrestamo(Prestamo('Balún Canán', 8, 9.50))
    u2.agregarPrestamo(Prestamo('Oficio de Tinieblas', 5, 12.00))
    u2.agregarPrestamo(Prestamo('Árbol de Literatura', 3, 18.00))

    u3.agregarPrestamo(Prestamo('El Llano en Llamas', 10, 7.50))

    # Registrar usuarios
    mi_biblio.agregarUsuario(u1)
    mi_biblio.agregarUsuario(u2)
    mi_biblio.agregarUsuario(u3)
    mi_biblio.agregarUsuario(u4)

    # Imprimir Reporte
    print(mi_biblio)
    print(f"Total de usuarios registrados : {len(mi_biblio.usuarios)}")
    print(f"Total de préstamos activos    : {mi_biblio.totalPrestamos()}")
    print("-" * 115)
    
    print("\n--- Catálogo de Usuarios Registrados ---")
    for u in mi_biblio.usuarios:
        print(u)

    print("\n--- Detalle de Préstamos por Lector ---")
    for u in mi_biblio.usuarios:
        print(f"\n{u.id_usuario} - {u.nombre:<18} | Costo Acumulado del Lector: ${u.totalTarifas():,.2f}")
        for p in u.prestamos:
            print(p)
    
    print("\n" + "=" * 115)
    print(f"IMPORTACIÓN TOTAL RECAUDADA POR LA BIBLIOTECA: ${mi_biblio.totalImportePrestamos():,.2f}")
    print("=" * 115)

if __name__ == '__main__':
    main()