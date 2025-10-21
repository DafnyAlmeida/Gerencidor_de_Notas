def verificar_situacao(med):
    if med >= 7:
        print("Aprovado")
    elif med >= 5 and med < 6.9:
        print("Se lascou")
    else:
        print("Desaprovado")

def calcular_media(lista):
    cont = 0
    for n in lista:
        cont += n
    n_itens = len(lista)
    media = cont/n_itens
    print(f"Sua média foi {media}")
    return verificar_situacao(media)