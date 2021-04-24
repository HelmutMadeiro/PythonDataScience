#Listas são coleções sequenciais, isto é, os itens destas sequências estão ordenados e utilizam índices
#(números inteiros) para acessar os valores.

#Os dicionários são coleções um pouco diferentes. São estruturas de dados que representam um tipo de mapeamento.
#Mapeamentos são coleções de associações entre pares de valores onde o primeiro elemento do par é conhecido
#como chave (key) e o segundo como valor (value).

#dicionario = {key_1: value_1, key_2: value_2, ..., key_n: value_n}

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

