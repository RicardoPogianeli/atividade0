
def menu():
    print("1 = Soma")
    print("2 = Subtração")
    print("3 = Divisão")
    print("4 = Multiplicação")

    opcao = int(input("Digite o valor wscolhido do menu"))
    return opcao

def soma():
    a = int (input("Digite o primeiro valor"))
    b = int (input("Digite o segundo valor"))

    result = a+b
    return result

def subtracao(a,b):
   return a-b

def divisao(a,b):
   return a/b

def multipicacao(a,b):
   return a*b


opc = menu()
if (opc == 1 ):
    print("O valor da soma é:", soma())
elif (opc == 2):
    a = int (input("Digite o primeiro valor"))
    b = int (input("Digite o segundo valo"))
    print("O valor da subtração é", subtracao(a,b))
elif (opc == 3):
    a = int (input("Digite o primeiro valor"))
    b = int (input("Digite o segundo valo"))
    print("O valor da Divisão é", divisao(a,b))
elif (opc == 4):
    a = int (input("Digite o primeiro valor"))
    b = int (input("Digite o segundo valo"))
    print("O valor da Multiplicação é", multipicacao(a,b))

