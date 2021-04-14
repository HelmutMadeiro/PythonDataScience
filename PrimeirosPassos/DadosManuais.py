from random import randrange

idades =[20,12,40]
permisoes =[]

def permisao_para_Dirigir (idades,permisoes):
   for idade in idades:
         if idade >=18:
            permisoes.append(True)
         else:
            permisoes.append(False)


permisao_para_Dirigir(idades,permisoes)

print(permisoes)

for permisao in permisoes:
     if permisao == True:
        print("Tem permisao")
     else:
         print("Não tem permisao")


# tipos em uma lista
lista = ['Guilerme',28,True,'18']
for elemento in lista:
    print (f'Elemento {elemento} é do tipo: ', type(elemento))
from typing import List

