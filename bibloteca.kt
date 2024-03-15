class Main
{

    val libro1: Libro = Libro ("LOTR" , "J.R.R" , "Tolkien" , 2)
    val libro2: Libro = Libro ("1984" , "George Orwell" , 20)

    val socio1: Socio = Socio ("Ruben" , "Rodriguez" , 101)
    val socio2: Socio = Socio ("Carlos" , "Bonilla" , 202)

    val prestamo1: Prestamo = Prestamo (libro1 , socio1 , "2024-03-15")
    val prestamo2: Prestamo = Prestamo (libro2 , socio2 , "2024-02-15")

    prestamo1.registrarPrestamo()
    libro1.informacion()
    socio1.informacion()
    prestamo1.devolverPrestamo()
    libro1.informacion()

}

fun main() {
    Main()


}
