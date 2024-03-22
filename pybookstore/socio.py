class Socio:
    def __init__(self, nombre: str, apellido: str, numero_socio: int):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_socio = numero_socio

    def solicitar_prestamo(self, libro: Libro, fecha_prestamo: str) -> None:
        print(f"Prestamo solicitado por {self.nombre} {self.apellido} , numero socio {self.numero_socio}")
        prestamo: Prestamo = Prestamo(libro, self)
        prestamo.registrarPrestamo(fecha_prestamo)

    def devolver_prestamo(self, libro: Libro) -> None:
        print(f"Devolucion de prestamo por $nombre $apellido, numero de socio: {self.numero_socio}")
