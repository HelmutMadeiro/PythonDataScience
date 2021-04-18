import numpy as np
anos    = np.loadtxt(fname = "data\carros-anos.txt", dtype = int)
km      = np.loadtxt(fname = "data\carros-km.txt")
valor   = np.loadtxt(fname = "data\carros-valor.txt")

#print (anos,km,valor)
anos.shape


dataset = np.column_stack((anos, km, valor))
print(dataset)
print(dataset.shape)

#Media
#estou fazendo a media por coluna  axis = 0 se quisersse linhas seria 1
print(np.mean(dataset, axis= 0))

#pegar por slise
print(np.mean(dataset[:, 2]))

#desvio padrão
print(np.std(dataset[:, 2]))

#soma
print(dataset[:, 1].sum())

print(dataset.sum(axis=0))