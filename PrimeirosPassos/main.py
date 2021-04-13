def saudacao(nome):
    return print(f'Olá  {nome} tudo bom?')


def verifica_se_pode_dirigir(idade):
    idade = int(idade)
    if idade >= 18:
        print("você tem idade para dirigir")
    else:
        print("Você não tem idade para dirigir")


nome = input('Qual seu nome? ')
saudacao(nome)

idade = input('qual a sua idade?')
erifica_se_pode_dirigir(idade)

idades = [1,22,3,44,5,66,7,88]

for idade in idades:
    verifica_se_pode_dirigir(idade)


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

















