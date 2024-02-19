
def generar_histograma():
    tirades = [0] * 11

for i in range(1,7):
    for j in range(1,7):
        suma_dados = i+j
        tirades[suma_dados] += 1