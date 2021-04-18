Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado','Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']
dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
dados

print(list(range(10)))

for item in Acessorios:
    print(item)

quadrado =[]

for i in range(10):
    quadrado.append(i**2)
print (quadrado)

print([1 ** 2 for i in range(10)])

Acessorio = []
for lista in dados:
    for item in lista:
        Acessorio.append(item)
print(Acessorio)
#list comprehensions
print(list(set([item for lista in dados for item in lista])))

#remode duplicado
list(set(Acessorio))

# 1º item da lista - Nome do veículo
# 2º item da lista - Ano de fabricação
# 3º item da lista - Veículo é zero km?


# usando o if e else
dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]


zero_km_y = []
for lista in dados:
    if(lista[2] == True):
        zero_km_y.append(lista)
print(zero_km_y)

zero_km_N = []
for lista in dados:
    if(lista[2] == False):
        zero_km_N.append(lista)
print(zero_km_N)

print([zero_km_y for lista in dados if lista[2] == True])


zero_km_y,zero_km_N = [],[]

for lista in dados:
    if(lista[2] == True):
        zero_km_y.append(lista)
    else:
        zero_km_N.append(lista)

print(zero_km_y,zero_km_N)


A, B, C = [],[],[]
for lista in dados:
    if lista[1]<=2000:
        A.append(lista)
    elif lista[1]> 2000 and lista[1] <=2010:
        B.append(lista)
    else:
        C.append(lista)

print(A)
print(B)
print(C)

A, B, C = [],[],[]
for lista in dados:
    if lista[1]<=2000:
        A.append(lista)
    elif (2000 > lista[1] <=2010):
        B.append(lista)
    else:
        C.append(lista)



pesos = [106.0, 68.5, 75.0]
alturas =[1.9, 1.53, 1.75]




imc.append(imcs)

print (imc)

import numpy as np
peso = np.array([106.0, 68.5, 75.0])
altura = np.array([1.9, 1.53, 1.75])
IMC = peso / altura ** 2
print(IMC)