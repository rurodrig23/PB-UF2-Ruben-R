#Registre de temperatures
temperatures = []
dia = 1
mes = 1

def mostrar_menu():
    ...

def tractar_opcio():
    ...

def resgistre_temperatures_setmanas():
    ...

def mostrar_mitjana():
    ...

def mostrar_diferencia():
    ...

def finalitzar_execucio():
    ...

def llegir_temperatures_teclat():
    lector = input("Escriu les temperatures d'aquesta setmana: ")
    for temperatura in lector.split():
        temperatures.append(float(temperatura.replace(',','.')))

def calcula_diferencia():
    ...

def calcular_mitjana():
    ...

def mostrar_data():
    print(dia, "de")
    if mes == 1:
        print()

def incrementar_data():
    diesAquestMes = 0
    dia += 7
    if mes == 2:
        diesAquestMes = 28
    elif mes in  [4,5,8,11]:
        diesAquestMes= 30
    else: 
        diesAquestMes = 31

    dia += 7
    if dia > diesAquestMes:
        dia = dia - diesAquestMes
        mes += 1

        if mes > 12:
            mes = 1

    print()