from time import time

import numpy as np
# buscar apenas uma funcao
# podemos importar somente as funções que iremos utilizar. Para isso,
# basta usarmos a instrução from seguida do nome da biblioteca,
# a palavra-chave import e a função desejada - nesse caso, arange().
from numpy import arange
np.arange(10)
km = np.array ([1000,2300,4987,1500])
print(km)

dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados



# importação de um txt
km = np.loadtxt(fname = 'data\carros-km.txt',dtype = int)
print (km)

Acessorios = np.array(dados)

print(dados)
#saber a dimensao do array (linas,colunas )
print(Acessorios.shape)
print(km.shape)



#é possivel fazer calculos nos arrays em np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = []
idade.append(2019 - anos)
print (idade)

km_media = km / idade
print(km_media)

dados = np.array([km,anos])

print(dados,'teste' )

#0 pego o primeira linha  arrei e 1 segunda linha
km_media = dados[0] / (2019 - dados[1])
print(km_media)

dados_new = dados.copy()
dados_new

dados_new.resize((3, 5))


dados_new.resize((3, 5), refcheck=False)
dados_new


dados_new[2] = dados_new[0] / (2019 - dados_new[1])
dados_new
