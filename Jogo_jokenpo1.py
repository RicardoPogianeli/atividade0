import random

def jogo(opcao_jogador):
    opcao_cpu = None
    nome_opcao_cpu = None
    nome_opcao_jogador = None
    random.randint(1,3)
    opcao_cpu = random.randint(1,3)

    convert_num_em_nome = {
        1: "papel",
        2: "pedra",
        3: "tesoura"}
    nome_opcao_cpu = convert_num_em_nome.get(opcao_cpu)
    nome_opcao_jogador = convert_num_em_nome.get(opcao_jogador)

    if opcao_jogador == opcao_cpu:
        print("Empate!!! vc jogou %s e o computador jogou %s"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 1 and opcao_cpu == 2:
        print("Voce Ganhou!!! vc jogou %s e o computador jogou %s"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 1 and opcao_cpu == 3:
        print("Voce Perdeu!! vc jogou %s e o computador jogou %s"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 2 and opcao_cpu == 1:
        print("Voce Perdeu!!! vc jogou %s e o computador jogou %s"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 2 and opcao_cpu == 3:
        print("Voce Ganhou!!! vc jogou %s e o computador jogou %s"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 3 and opcao_cpu == 1:
        print("Voce Perdeu!!!vc jogou %s e o computador jogou %s"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 3 and opcao_cpu == 2:
        print("Voce Perdeu!!! vc jogou %s e o computador jogou %s"%(nome_opcao_jogador,nome_opcao_cpu))

def menu():
    # Papel = 1
    # Pedra = 2
    # Tesoura = 3
    opcao_digitada = None
    quantidade_jogo = 0
    while opcao_digitada is None:
        print("Por favor, digite as seguinte opcoes: 1 = Papel, 2 = Pedra, 3 = Tesoura")
        opcao_digitada = int(input("Digite um Número:"))

        if opcao_digitada == 1:
            print("Papel")
        elif opcao_digitada == 2:
            print("Pedra")
        elif opcao_digitada == 3:
            print("Tesoura")
        else:
            print("%s: Voce digitou um numero invalido. Fim do Jogo!!!"%opcao_digitada)
            print("Voce jogou %s vezes" %quantidade_jogo)
            break
        jogo(opcao_digitada)
        opcao_digitada = None
        quantidade_jogo = quantidade_jogo + 1

    return opcao_digitada

menu()













