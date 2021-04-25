#Listas são coleções sequenciais, isto é, os itens destas sequências estão ordenados e utilizam índices
#(números inteiros) para acessar os valores.

#Os dicionários são coleções um pouco diferentes. São estruturas de dados que representam um tipo de mapeamento.
#Mapeamentos são coleções de associações entre pares de valores onde o primeiro elemento do par é conhecido
#como chave (key) e o segundo como valor (value).

#dicionario = {key_1: value_1, key_2: value_2, ..., key_n: value_n}
from typing import Dict, List, Union

carros = ['Jetta Variant', 'Passat', 'Crossfox']
carros
valores = [88078.64, 106161.94, 72832.16]
valores

#uma forma de criar um dicionario de dados
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados

#outra forma de criar um dicionario de dados
dados = dict(zip(carros, valores))
dados

#Se buscarmos por uma chave que não está presente no dicionário, o retorno será False.
'Fusca' in dados

#A função len(), ao receber um dicionário como parâmetro, consegue nos devolver o tamanho (número de itens) de um dicionário.
len(dados)

# inclusao
dados['DS5'] = 124549.07
dados

#deletar
del dados['Passat']
dados


dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    },
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

#atualiza o dicionario
dados.update({'Passat':106161.95,'Fusca': 150000,'DS5': 124549.07})

#faz uma copia e aloca em outra parte da memoria
dadosCopy = dados.copy()

#deleta o que colocar na chave
del dadosCopy['Fusca']
print(dadosCopy)
print(dados)

#deleta do dicionado e exibe oque foi elimidado
dadosCopy.pop('Passat')

#deleta do dicionado e exibe oque foi elimidado, caso nao econtre exibe o segundo paramentro
dadosCopy.pop('Passat','Chave nao encontrada')
print(dadosCopy)

# limpa o dicionario
dadosCopy.clear()
print(dadosCopy)

dados = {'Crossfox': 72832.16, 'DS5': 124549.07,  'Fusca': 150000,  'Jetta Variant': 88078.64,  'Passat': 106161.95}

#retona uma lista contendo as chaves do dicionaio
print(dados.keys())

for key in dados.keys():
   print(dados[key])

for item in dados.items():
    print(item)

for key, value in dados.items():
    print(key,value)

for key, value in dados.items():
    if value > 100000:
        print(key)

dados = {
    'Crossfox': {'valor': 72000, 'ano': 2005},
    'DS5': {'valor': 125000, 'ano': 2015},
    'Fusca': {'valor': 150000, 'ano': 1976},
    'Jetta': {'valor': 88000, 'ano': 2010},
    'Passat': {'valor': 106000, 'ano': 1998}
}

print(dados)

for item in dados.items():
    if(item[1]['ano'] >= 2000):
        print(item[0])

dados = {'Crossfox': 72832.16, 'DS5': 124549.07,  'Fusca': 150000,  'Jetta Variant': 88078.64,  'Passat': 106161.95}

valores = []
for valor in dados.values():
    valores.append(valor)

print(valores)

soma = 0

for valor in dados.values():
    soma += valor
print(soma)

# ou
print(sum(dados.values()))

