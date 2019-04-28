dia_nascimento = input("Qual dia de Nascimento?")
mes_nascimento = input("Em que mês você nasceu?")
soma = int(dia_nascimento) + int(mes_nascimento) + int(100)
print ('Escolha um número entre 100 e {}!'.format(soma))

escolha = int(input("Escolha o Número:"))

while escolha < 100 or escolha > soma:
    print("Digite um Número Válido")
    escolha = int(input("Escolha o Número:"))

nome = input("Qual seu Nome?")
sobrenome = input("Qual seu Sobrenome?")
ano = input("Em que ano você nasceu?")

for i in range(1, escolha):
    if i%3==0 and i%5==0 :
        print(ano)
    elif i%3==0:
        print(nome)
    elif i% 5==0:
        print (sobrenome)

    else:
        print(i)



#print(nome)







