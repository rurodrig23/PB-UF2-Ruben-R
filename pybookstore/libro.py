class Libro:
    def __init__(self,titulo: str, autor: str, ejemplares_disponibles: int):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

    def prestar(self) -> None:
        if self.ejemplares_disponibles > 0:
            self.ejemplares_disponibles -= 1
            print(f"Libro prestado: {self.titulo}, Autor: {self.autor}")
        else:
            print(f"No hay ejemplares disponibles de {self.titulo}")

    def devolver(self) -> None:
        self.ejemplares_disponibles += 1
        print(f"Libro devuelto: {self.titulo}")
        
    def informacion(self):
        print(f"Titulo: {self.titulo}, Ejemplares disponibles {self.ejemplares_disponibles}")
