temperaturas_registradas = []
temperaturas = []
def calcul_mit(temperaturas):
    if not temperaturas:
        print("No hay temperaturas registradas.")
        return
    
    suma_temperaturas = 0
    for temp in temperaturas:
        suma_temperaturas += temp
    
    media = suma_temperaturas / len(temperaturas)
    print(f"La temperatura media es: ")

def val_temp(temperaturas):

    try:
        temperaturas_float = [float(temp) for temp in temperaturas.split()]
        return temperaturas_float
    except ValueError:
        print("Error: Se deben ingresar valores numéricos.")
        return None
    except ValueError:
        print("Error: Se deben ingresar valores numericos")
        return None
    
def cal_dif_max(temperaturas):
    if not temperaturas:
        print("No hay temperaturas registradas.")
        return
    
    if len(temperaturas) < 2:
        print("Debe haber al menos dos temperaturas registradas para calcular la diferencia máxima.")
        return
    
temperatura_minima = temperatura_maxima = temperaturas_registradas[0]
for temp in temperaturas:
        if temp < temperatura_minima:
            temperatura_minima = temp
        elif temp > temperatura_maxima:
            temperatura_maxima = temp
    
diferencia_maxima = temperatura_maxima - temperatura_minima
print(f"La diferencia máxima entre temperaturas hasta la fecha es: {diferencia_maxima:.2f} grados Celsius.")

def menu():
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
                temperaturas_registradas.extend(temperaturas_validadas)
                print("Temperatures registrades amb èxit.")
        elif opcion == "MJ":
            calcul_mit(temperaturas_registradas)
        elif opcion == "DF":
            cal_dif_max(temperaturas_registradas)
        elif opcion == "FI":
            print("Gràcies per utilitzar el registre de temperatures. ")
            break
        else:
            print("Opció no vàlida. ")