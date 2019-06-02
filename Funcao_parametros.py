lista_num =[]
for num in range(1,20):
   lista_num.append(int(input("Digite um número")))
print (lista_num)

# Crie uma função que receba o vetor preenchido e substitua todas as ocorrências de valores negativos por 0, as de valores menores do que 10 por 1 e as demais por 2.

def numero_negativo(lista):
   negativo = []
   for item in lista:
      if item < 0:
         negativo.append(0)
      elif item < 10:
         negativo.append(1)
      else:
         negativo.append(2)

   return negativo

print(numero_negativo(lista_num))






