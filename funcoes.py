def verificar_situacao(med):
    if med >= 7:
        return "Aprovado"
    elif med >= 5 and med < 6.9:
        return "Se lascou"
    else:
        return "Desaprovado"

def calcular_media(lista):
    cont = 0
    for n in lista:
        cont += n
    n_itens = len(lista)
    medi = cont/n_itens
    return medi