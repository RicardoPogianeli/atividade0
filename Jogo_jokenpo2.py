import random

def placar(lista_placar):
    quantidade_Vitoria = 0
    quantidade_Derrota = 0
    quantidade_Empate = 0
    total_partidas = len(lista_placar)
    num_index = 0
    for item in lista_placar:
        #print(item)
        if item == "Vitoria":
            quantidade_Vitoria = quantidade_Vitoria + 1
        elif item == "Derrota":
            quantidade_Derrota = quantidade_Derrota + 1
        elif item == "Empate":
            quantidade_Empate = quantidade_Empate + 1
    porcentagem_Vitoria= ((quantidade_Vitoria / total_partidas)*100)
    porcentagem_Derrota= ((quantidade_Derrota / total_partidas)*100)
    porcentagem_Empate= ((quantidade_Empate / total_partidas)*100)
    print("Voce venceu %s %% de %s partidas!"%(porcentagem_Vitoria,total_partidas))
    print("Voce Perdeu %s %% de %s partidas!"%(porcentagem_Derrota,total_partidas))
    print("Voce empatou %s %% de %s partidas!" % (porcentagem_Empate, total_partidas))
    print("\nResultado de todas partidas: \n")
    for item in lista_placar:
        num_index = num_index + 1
        print("Partida %s voce obteve uma: %s "%(num_index,item))


#a = ["Vitoria", "Derrota", "Empate"]

#placar(a)

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
    resultado_jogo = None

    if opcao_jogador == opcao_cpu:
        resultado_jogo = "Empate"
        print("Empate!!! vc jogou %s e o computador jogou %s\n"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 1 and opcao_cpu == 2:
        resultado_jogo = "Vitoria"
        print("Voce Ganhou!!! vc jogou %s e o computador jogou %s\n"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 1 and opcao_cpu == 3:
        resultado_jogo = "Derrota"
        print("Voce Perdeu!! vc jogou %s e o computador jogou %s\n"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 2 and opcao_cpu == 1:
        resultado_jogo = "Derrota"
        print("Voce Perdeu!!! vc jogou %s e o computador jogou %s\n"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 2 and opcao_cpu == 3:
        resultado_jogo = "Vitoria"
        print("Voce Ganhou!!! vc jogou %s e o computador jogou %s\n"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 3 and opcao_cpu == 1:
        resultado_jogo = "Derrota"
        print("Voce Perdeu!!!vc jogou %s e o computador jogou %s\n"%(nome_opcao_jogador,nome_opcao_cpu))
    elif opcao_jogador == 3 and opcao_cpu == 2:
        resultado_jogo = "Derrota"
        print("Voce Perdeu!!! vc jogou %s e o computador jogou %s\n"%(nome_opcao_jogador,nome_opcao_cpu))
    return resultado_jogo

def menu():
    # Papel = 1
    # Pedra = 2
    # Tesoura = 3
    opcao_digitada = None
    quantidade_jogo = 0
    resultado_lista = []
    while opcao_digitada is None:
        print("Por favor, digite as seguinte opcoes: 1 = Papel, 2 = Pedra, 3 = Tesoura")
        opcao_digitada = int(input("Digite um Número: "))

        if opcao_digitada == 1:
            print("Papel \n")
        elif opcao_digitada == 2:
            print("Pedra\n")
        elif opcao_digitada == 3:
            print("Tesoura\n")
        else:
            print("%s: Voce digitou um numero invalido. Fim do Jogo!!!\n"%opcao_digitada)
            print("Voce jogou %s vezes!" %quantidade_jogo)
            placar(resultado_lista)
            break
        resutado_jogo = jogo(opcao_digitada)
        resultado_lista.append(resutado_jogo)
       #print(resultado_lista)
        opcao_digitada = None
        quantidade_jogo = quantidade_jogo + 1

    #return opcao_digitada

menu()


