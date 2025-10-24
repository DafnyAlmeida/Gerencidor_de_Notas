from funcoes import *
import emoji

relatorio = {}

while True: 
    
    print("Bem-vindo ao sistema de notas")
    print("1 – Cadastrar aluno e notas")
    print("2 – Exibir relatório")
    # print("3 - Pesquisar um aluno especifico")
    print("0 – Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        nome = input("Digite o nome do aluno: ")
        notas = []
        for i in range(1, 4):
            nota = int(input(f"Digite a {i}º nota: "))
            notas.append(nota)
        
        media = calcular_media(notas)
        situacao = verificar_situacao(media)
        
        relatorio[nome] = {
            "notas": notas,
            "media": media,
            "situacao": situacao
        }
        
        print(emoji.emojize(f"Aluno {nome} cadastrado com sucesso :thumbs_up:"))
        
    if opcao == 2:
        print(f"O relatorio é: {relatorio}")
    
    # if opcao == 3:
    #     if not relatorio:
    #         print("Nenhum aluno cadastrado ainda.")
    #     else:
    #         nome = input("Digite o nome do aluno que deseja consultar: ")
    #         if nome in relatorio:
    #             dados = relatorio[nome]
    #             print(f"\nAluno: {nome}")
    #             print(f"Notas: {dados['notas']}")
    #             print(f"Média: {dados['media']:.2f}")
    #             print(f"Situação: {dados['situacao']}")
    #         else:
    #             print("Aluno não encontrado.")
    
    if opcao == 0:
        print("Programa finalizado.")
        break

    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 0:
        print("Opção inválida, tente novamente.")