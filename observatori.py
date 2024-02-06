
def calcul_mit(dades_enregistrades):
    if not dades_enregistrades:
        print("No hay temperaturas registradas.")
        return
    
    suma_temperaturas = 0
    for temp in dades_enregistrades:
        suma_temperaturas += temp
    
    media = suma_temperaturas / len(dades_enregistrades)
    print(f"La temperatura media hasta la fecha es: {media:.2f} grados Celsius.")

def val_temp(dades_enregistrades):

    try:
        temperaturas_float = [float(temp) for temp in dades_enregistrades.split()]
        return temperaturas_float
    except ValueError:
        print("Error: Se deben ingresar valores numéricos.")
        return None

#def temp_reg():
     
#def cal_dif_max():


def menu():
    dades_enregistrades = []

while True:
        print("\nBenvingut al registre de temperatures")
        print("[RT] Registrar temperatures setmanals.")
        print("[MJ] Consultar temperatura mitjana.")
        print("[DF] Consultar diferència màxima.")
        print("[FI] Sortir.")
        opcion = input("Opció: ").upper()
        
        if opcion == "RT":
            temperaturas_semana = input("Escriu les temperatures d'aquesta setmana (separades per espais): ")
            temperaturas_validadas = val_temp(temperaturas_semana)
            if temperaturas_validadas:
                temp_reg.extend(temperaturas_validadas)
                print("Temperatures registrades amb èxit.")
        elif opcion == "MJ":
            calcul_mit(temp_reg)
        elif opcion == "DF":
            cal_dif_max(temp_reg)
        elif opcion == "FI":
            print("Gràcies per utilitzar el registre de temperatures. ")
            break
        else:
            print("Opció no vàlida. ")