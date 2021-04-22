nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])

print (nomes_carros[1:3])

# varrer cada um dos itens
for item in nomes_carros:
    print(item)

#Desempacotamento de tuplas

carro_1 ,carro_2 ,carro_3 ,carro_4  = nomes_carros

print(carro_1)

_,A,_,B = nomes_carros

print(A,B)

_,C,*_ = nomes_carros

print(C)

carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
carros
valores = [88078.64, 106161.94, 72832.16, 124549.07]
valores
zip(carros, valores)
print(list(zip(carros, valores)))

for carro, valor in zip(carros, valores):
  if(valor > 100000):
    print(carro)

#Alternativa correta! Note que no segundo laço for, utilizamos as listas de acessórios como iterador.
carros = (
    (
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
    ),
    (
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
    )
)

for t in carros:
    for i in t[-1]:
        print(i)

#Duas ferramentas bastante utilizadas quando iteramos com tuplas são o desempacotamento
#de tuplas e a built - in function zip(). Com o desempacotamento de tuplas, é possível
#fazer declarações conjuntas de variáveis e utilizar cada variável individualmente.Por
#exemplo:

nome, valor = ('Passat', 100000.0)
nomes = ['Passat', 'Crossfox']
valores = [100000.0, 75000.0]
list(zip(nomes, valores))