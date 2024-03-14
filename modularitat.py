class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def moure_dreta(self):
        self.x += 1
    
    def moure_esquerra(self):
        self.x -= 1
    
    def moure_amunt(self):
        self.y += 1
    
    def moure_avall(self):
        self.y -= 1

# Coordenada inicial
coordenada = Coordenada(0, 0)

# Ejecutar movimientos
coordenada.moure_dreta()
print(f"Nueva coordenada después de mover a la derecha: ({coordenada.x}, {coordenada.y})")

coordenada.moure_amunt()
print(f"Nueva coordenada después de mover arriba: ({coordenada.x}, {coordenada.y})")
