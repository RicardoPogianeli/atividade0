'''lista_num = []
num_digitado = None

while num_digitado != 0:
   try:
      num_digitado = int(input("Digite um Número:"))

      if num_digitado > 0 :
         lista_num.append(num_digitado)
   except Exception as e:
      print("caracter digitado e invalido")
print(lista_num)




def determinar_primo(lista):
   primos = []
   for item in lista:
      if item%2==1:
         primos.append(item)

   return primos


print (determinar_primo(lista_num))
'''

lista_num =[]
num_digitado = None
