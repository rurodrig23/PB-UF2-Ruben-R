class coordenada() {

    constructor():
        this.x = x
        this.y = y

    fun moureDreta() {
        this.x += 1
    }
    
    fun moureEsquerra() {
        this.x -= 1
    }
    
    fun moureAmunt() {
        this.y += 1
    }
    
    fun moureAvall() {
        this.y -= 1
    }
}

// Coordenada inicial
var coordenada = coordenada(0, 0)

// Ejecutar movimientos
coordenada.moureDreta()
println("Nova coordenada després de moure a la dreta: (${coordenada.x}, ${coordenada.y})")

coordenada.moureAmunt()
println("Nova coordenada després de moure amunt: (${coordenada.x}, ${coordenada.y})")
