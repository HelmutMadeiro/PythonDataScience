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
verifica_se_pode_dirigir(idade)
