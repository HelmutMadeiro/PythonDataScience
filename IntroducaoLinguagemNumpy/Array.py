import numpy as np
# Vamos criar um array com 2 dimensões
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2d)

# Podemos acessar cada dimensão da seguinte forma
print('index 2 ', arr2d[2] )

# Selecionamos o elemento com índice 2, e desse  elemento o sub-elemento com índice 1
print(arr2d[2][1])
# A sintaxe acima é equivalente a esta abaixo
print(arr2d[2,1])
# Criando um array com 3 dimensões
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print('Arry com 3D \n', arr3d , '\n FIM ')
#[
#    0[
#        0[ 1  2  3]
#        1[ 4  5  6]
#     ]
#    1[
#        0[ 7  8  9]
#        1[10 11 12]
#     ]
#]


# Selecionando o primeiro elemento (índice 0).
print(arr3d[0])
#[
#    [1 2 3]
#    [4 5 6]
#]
# Selecionando o elemento com índice 1 e o sub-elemento com índice 0.
print( arr3d[1, 0])

#[7 8 9]

# Da mesma forma, selecionamos o elemento final com os seguintes índices
print(arr3d[1, 0, 2])
#9


idades = np.array([10, 23, 45, 34, 25])
np.sum(idades) / idades.size
np.mean(idades)

idades.mean()
