import numpy as np

km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

dados = np.array([km, anos])

contador = np.arange(10)
print(contador)

item = 6
item = item - 1
print(contador[item])
print(dados[1][2])
print(dados[1, 2])

print(contador[1:4])
print(contador[1:8:2])
print(contador[::2])
print(contador[1::2])

print(dados[:,1:3][0])
print(dados[:,1:3][1])
print(2019 - dados[:,1:3][1])
print(dados[:,1:3][0] /(2019 - dados[:,1:3][1]))

print(contador > 5)
# [False False False False False False  True  True  True  True]

print(contador [contador > 5])
#[True  True  True  True]
# [6,7,8,9]

#[
#0 [44410.,  5712., 37123.,      0.,  25757.]
#        0,      1,      2,       3,      4
#1 [ 2003.,  1991.,  1990.,  2019.,   2006.]
#        0,      1,      2,       3,      4
#] dados

#0 [44410.,  0.,  25757.]
#        0,         3,      4
#1 [ 2003.,   2019.,   2006.]

print(dados [:, dados [1] > 2000])

#0 [44410.,  0.,  25757.]
#        0,         3,      4
#1 [ 2003.,   2019.,   2006.]

dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'], ['Sheila', 'solteiro', 'feminino'], ['Bruno', 'solteiro', 'masculino'], ['Rita', 'casado', 'feminino']
    ]
)

#[
#    ['Roberto', 'casado', 'masculino'],
#    ['Sheila', 'solteiro', 'feminino'],
#    ['Bruno', 'solteiro', 'masculino'],
#    ['Rita', 'casado', 'feminino']
#]
print(dados.shape)

#(4, 3)
#dados[todas as linhas ,apenas colunas 0,1 ]
resultado_primeiro_slice = dados[:,0:2]

print(resultado_primeiro_slice)

#total de linhas apenas a utima coluna  onde  seja masculino
print(dados[:,-1]=='masculino')

# traga aonde eh verdadeiro dentro do array
print(resultado_primeiro_slice[dados[:,-1]=='masculino'])


