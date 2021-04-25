
#sem paramentros
def media():
    valor = (1+2+3)/3
    print(valor)

print (media())

def media(n1,n2,n3):
    valor = (n1+n2+n3) / 3
    print(valor)

print(media(1,2,3))

def media(lista):
    valor = sum(lista)/len(lista)
    print(valor)

resultado = media([123324,342,425435])
print (resultado,'nao aparece resultado')

def media(lista):
    valor = sum(lista)/len(lista)
    return valor

print(media([123324,342,425435]))


def media(lista):
    valor = sum(lista) / len(lista)
    return valor,len(lista)


print(media([123324, 342, 425435]))

media, totalElemento = media ([123324, 342, 425435])

print (media, totalElemento)

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979},
    'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual): # criando com dois paramentros
    for item in dataset.items(): #passando e pegando itens e coloando no item
        result = item[1]['km'] / (ano_atual - item[1]['ano'])  # [1] pega a lista 1 com a chave km / pelo
                                                               #cheve ano - o ano atual
        print(result)

print(km_media(dados,2019))


def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        result.update({item[0]:media})
    return result

print(km_media(dados,2019))


dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979},
    'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999}
}

def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })
    return result

print(km_media(dados,2019))
