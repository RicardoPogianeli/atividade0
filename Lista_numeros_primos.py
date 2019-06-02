lista_num = []
num_digitado = None

while num_digitado != 0:
   try:
      num_digitado = int(input("Digite um Número:"))

      if num_digitado > 0 :
         lista_num.append(num_digitado)
   except Exception as e:
      print("caracter digitado e invalido")
print(lista_num)

'''
Para cada numero da lista verifique se ele e primo e Imprima
'''

def determinar_primo(lista):
   primos = []
   for item in lista:
      if item%2==1:
         primos.append(item)

   return primos


print (determinar_primo(lista_num))




