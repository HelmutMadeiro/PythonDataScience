import pandas as pd
carros = ['jetta variant', 'Passat', 'Crossfox']

#as series, arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado.
#Os rótulos das linhas de uma series são conhecidos como index,

pd.Series(carros)

dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

dataset3 = pd.DataFrame(dados)

pd.set_option('display.max_rows',10)
pd.set_option('display.max_columns',100)

dataset = pd.read_csv ('dados/db.csv',sep =';',index_col=0)

dataset = pd.DataFrame(dataset)
#dataset.dtypes
#dataset.info()
#dataset[['Quilometragem','Valor']].describe()



dataset.head(2)
print(dataset[['Valor']])



