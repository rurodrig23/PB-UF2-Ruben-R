

def operaciones_tem():




def calcul_mit():

def val_temp():

def temp_reg():
     
def cal_dif_max():


def menu():
    dades_enregistrades = [20,5 21,1 21 21,7 20,9 20,6 19,9 ]

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
            print("Opció no vàlida. Si us plau, trieu una opció correcta.")



def sortida():       