pizzeria = []
estoc_ingredients = {"tomate": 100, "formatge": 50, "pepperoni": 20}

def agregar_comanda(pizzeria):
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        pizzas = input("tipo de pizza: ")
        total = input("total de importe: ")
        pagado = True
        comanda = {"nombre_cliente": nombre_cliente, "pizzas": pizzas.split(','), "total": total, "pagado": pagado}
        pizzeria.append(comanda)
        print(f'Comanda de "{nombre_cliente}" agregada a la pizzería.')


def preparacion_pizza(pizzeria):
        titulo = input("Ingrese el título del libro a prestar: ")
        encontrado = False
        for libro in biblioteca:
            if libro["titulo"] == titulo and libro["disponibilidad"]:
                libro["disponibilidad"] = False
                print(f'Libro "{titulo}" prestado con éxito.')
                encontrado = True
                break
        if not encontrado:
            print(f'Libro "{titulo}" no disponible para préstamo.')

def gestionar_estoc():
    print("Estoc d'ingredients:")
    for ingredient, quantitat in estoc_ingredients.items():
        print(f'{ingredient}: {quantitat}')


def salir():
     print("saliendo del programa")

while True:
    print("\n1. Agregar comanda")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_comanda(pizzeria)

    elif opcion == "2":
        preparacion_pizza()

    elif opcion == "3":
        estoc()
     
    elif opcion == "4":
        salir()
        break
    else:
         print("Opcion, no valida")