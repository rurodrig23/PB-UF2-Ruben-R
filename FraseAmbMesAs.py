def contar_letras_a(frase):
    count = 0
    for caracter in frase:
        if caracter.lower() == 'a':
            count += 1
    return count

def frase_amb_mes_as():
    while True:
        max_as = 0
        frase_mes_as = ""
        frase = input("Escribe una frase:\n> ")
        

        if frase.lower() == "fi":
            break
   
        num_as = contar_letras_a(frase)
        if num_as > max_as:
            max_as = num_as
            frase_mes_as = frase

        print(f'La frase amb més \'a\' és: "{frase_mes_as}"')
        print(f'Té {max_as} \'a\'.')
    

