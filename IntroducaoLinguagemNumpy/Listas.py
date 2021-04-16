Acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado',
              'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']


Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False,
           ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'],
           106161.94]

Carros = [Carro_1 , Carro_2]

A = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro']
B = ['Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

#A[i]
#Retorna o i-ésimo item da lista A.
#lista comeca em 0 e o ultimo é -1
print('primeiro item da lista  é {} e o ultimo é {}'.format(Acessorios[0],Acessorios[-1]))

#carros contem uma soma de lista dentro de lista

#o primeiro [0]  acesso o primeiro objeto que é uma lista
#o segundo  [-2] acesso o penultimo objet que é uma lista tbm
#o teceiro  [1]  acesso o segundo objeto que é uma lista tbm
print(Carros[0][-2][1])


#A[ i : j ]
#Recorta a lista A do índice i até o j. Neste fatiamento o elemento
# com índice i é incluído e o elemento com índice j não é incluído no resultado.

print('Busco aqui do treceiro elemento ate o 5 mas nao incluo',Acessorios[2:5])

print('Busco aqui do treceiro elemento ate o final ',Acessorios[2:])

print('Busco aqui aparti do elemento 5 ate o final mas nao  incluo o ultimo',Acessorios[:5])


# ordernar uma lista
Acessorios.sort()
print(Acessorios)

# append adiciona mais um no seu objeto
Acessorios.append('4 x 4')
print(Acessorios)

#remover o ultimo da minha lista ou remove o que vc colocar no index
Acessorios.pop()
print(Acessorios)


#copy

#Aqui se vc modificar a variavel Acessorios ira modificar tbm a Acessorios_2
#Aqui se vc modificar a variavel Acessorios_ ira modificar tbm a Acessorios
Acessorios_2 = Acessorios
Acessorios_2.append('4 x 4')
print(Acessorios_2)
print(Acessorios)

# usando o copy aqui ele copia o que esta na memoria e nao modifica o original
Acessorios_2 =  Acessorios.copy()
Acessorios_3 =  Acessorios[:]
Acessorios_2.append('4 x 4')
print(Acessorios_3)
print(Acessorios_2)
print(Acessorios)















#estaNalista = 'Rodas de liga' in Acessorios
#if estaNalista == True:
#    print('Esta na lista')
#else:
 #   print('nao esta na lista')

#estaNalista = '4 x4' not in Acessorios
#if estaNalista == True:
  #  print('Esta na lista')
#else:
   # print('nao esta na lista')

#print('Existem {}'.format(len(A + B)), 'Dentro dessa lista que são ', A + B)
