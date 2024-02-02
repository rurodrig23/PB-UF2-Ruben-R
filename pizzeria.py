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

''''
def preparacion_pizza(pizzeria,estoc_ingredients):
    for comanda in pizzeria:
        if not comanda["pagat"]:
 '''           
def gestionar_stock():
    print("Estoc d'ingredients:")
    for ingredient, quantitat in estoc_ingredients.items():
        print(f'{ingredient}: {quantitat}')

def procesament_pagament():
   

def salir():
     print("saliendo del programa")

while True:
    print("\n1. Agregar comanda")
    print("2. Preparacion pizza")
    print("3. Gestionar stock de ingredientes")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_comanda(pizzeria)

    elif opcion == "2":
        preparacion_pizza()

    elif opcion == "3":
        gestionar_stock()

    elif opcion == "4":
        procesament_pagament()
     
    elif opcion == "5":
        salir()
        break
    else:
         print("Opcion, no valida")