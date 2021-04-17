
import numpy as np
peso = np.array([106.0, 68.5, 75.0])
altura = np.array([1.9, 1.53, 1.75])


for p in peso:
    for a in altura:
        print( p,a)

x = p / altura ** 2
print(a,p,x, 'aaa')
