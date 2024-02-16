def contar_letras_a(frase):
    count = 0
    for caracter in frase:
        if caracter.lower() == 'a':
            count += 1
    return count

def frase_amb_mes_as():
    max_as = 0
    frase_mes_as = ""

