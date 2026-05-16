#p161-control-libros
#El objetivo es desarrollar un sistema de control de préstamos de libros estructurado bajo el paradigma de Programación Orientada a Objetos en Python.

class Prestamo:
    def __init__(self, libro, dias, tarifa_diaria):
        self.libro = libro
        self.dias = dias
        self.tarifa_diaria = tarifa_diaria
        # El total se calcula automáticamente
        self.total = dias * tarifa_diaria

    def __str__(self):
        return f"-> Libro: {self.libro:<22} Dias: {self.dias:>3}  Tarifa/Día: $ {self.tarifa_diaria:>6.2f}  Total: $ {self.total:>8.2f}"


class Usuario:
    def __init__(self, id_usuario, nombre, correo, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.prestamos = []  # Lista de objetos de la clase Prestamo

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
        self.usuarios = []  # Lista de objetos de la clase Usuario

    def agregarUsuario(self, usuario):
        self.usuarios.append(usuario)

    def totalPrestamos(self):
        # Cuenta la cantidad de libros prestados en total
        total_libros = 0
        for u in self.usuarios:
            total_libros += len(u.prestamos)
        return total_libros

    def totalImportePrestamos(self):
        # Suma el dinero total de todos los usuarios
        total_dinero = 0
        for u in self.usuarios:
            total_dinero += u.totalTarifas()
        return total_dinero

    def __str__(self):
        header = "=" * 115
        info = f"REPORTE DE CONTROL DE PRÉSTAMOS: Biblioteca -> [Nombre: {self.nombre}  Domicilio: {self.domicilio}\nEncargado: {self.encargado}]"
        return f"{header}\n{info}\n{header}"


def main():
    # 1. Crear la Biblioteca
    mi_biblioteca = Biblioteca("Mauricio Magdaleno", "Calle Grillo 100, Col. Centro", "Dra. Leticia Ramírez")

    # 2. Crear Usuarios
    u1 = Usuario("USR-2026-X", "Salvador Novo", "snovo@cultura.gob.mx", "4921112233")
    u2 = Usuario("USR-2026-Y", "Amparo Dávila", "amparo@unam.mx", "4922223344")
    u3 = Usuario("USR-2026-Z", "Juan Rulfo", "jrulfo@literatura.mx", "4923334455")
    u4 = Usuario("USR-2026-W", "Elena Garro", "egarro@escritores.org", "4924445566")

    # 3. Agregar préstamos a los usuarios
    # Préstamos de Salvador Novo
    u1.agregarPrestamo(Prestamo("Laberinto de la Soledad", 6, 11.50))
    u1.agregarPrestamo(Prestamo("Pedro Páramo", 4, 14.00))

    # Préstamos de Amparo Dávila
    u2.agregarPrestamo(Prestamo("Balún Canán", 8, 9.50))
    u2.agregarPrestamo(Prestamo("Oficio de Tinieblas", 5, 12.00))
    u2.agregarPrestamo(Prestamo("Árbol de Literatura", 3, 18.00))

    # Préstamos de Juan Rulfo
    u3.agregarPrestamo(Prestamo("El Llano en Llamas", 10, 7.50))

    # 4. Registrar usuarios en la biblioteca
    mi_biblioteca.agregarUsuario(u1)
    mi_biblioteca.agregarUsuario(u2)
    mi_biblioteca.agregarUsuario(u3)
    mi_biblioteca.agregarUsuario(u4)

    # --- IMPRESIÓN DEL REPORTE (Basado en el ejemplo de la imagen) ---
    print(mi_biblioteca)
    print(f"Total de usuarios registrados : {len(mi_biblioteca.usuarios)}")
    print(f"Total de préstamos activos    : {mi_biblioteca.totalPrestamos()}")
    print("-" * 115)
    
    print("\n--- Catálogo de Usuarios Registrados ---")
    for u in mi_biblioteca.usuarios:
        print(u)

    print("\n--- Detalle de Préstamos por Lector ---")
    for u in mi_biblioteca.usuarios:
        print(f"\n{u.id_usuario} - {u.nombre:<18} | Costo Acumulado del Lector: ${u.totalTarifas():.2f}")
        for p in u.prestamos:
            print(p)
    
    print("\n" + "=" * 115)
    print(f"IMPORTACIÓN TOTAL RECAUDADA POR LA BIBLIOTECA: ${mi_biblioteca.totalImportePrestamos():.2f}")
    print("=" * 115)

if __name__ == "__main__":
    main()