import pandas as pd
pd.set_option('display.max_rows',10)
pd.set_option('display.max_columns',100)

dataset = pd.read_csv ('dados/db.csv',sep =';')

print(dataset.dtypes)
print(dataset.info())
print(dataset[['Quilometragem','Valor']].describe())

















