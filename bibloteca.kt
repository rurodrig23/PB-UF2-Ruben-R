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


class Libro(val titulo: String, val autor: String) {

    fun informacion() {
        println("Título: $titulo, Autor: $autor")
    }

    fun prestar() {
        println("Se ha prestado un ejemplar de $titulo")
    }

    fun devolver() {
        println("Se ha devuelto un ejemplar de $titulo")
    }
}




class Socio(val nombre: String, val apellido: String, val numeroSocio: Int) {

    fun informacion() {
        println()

class Prestamo

fun main() {
    Main()


}
