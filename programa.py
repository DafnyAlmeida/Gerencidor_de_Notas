from funcoes import *

while True: 
    rela = {}
    lista_notas = []
    print("Bem vindo ao nao sei")
    print("1 – Cadastrar aluno e notas")
    print("2 – Exibir relatório")
    print("0 – Sair")
    opcao = int(input("Escolha uma: "))
    if opcao == 1:
        nome = input("Digite o nome do aluno: ")
        rela[nome]
        for i in range(1, 4):
            nota = int(input(f"Digite a {i}º nota"))
            lista_notas.append(nota)
        rela[nome] = lista_notas
    if opcao == 2:
        media2 = calcular_media(lista_notas)
        print(f"Relatorio: {rela}, sendo a media igual a média e a situação a seguinte {media2}")
    if opcao == 0:
        print("Programa finalizado")
        break