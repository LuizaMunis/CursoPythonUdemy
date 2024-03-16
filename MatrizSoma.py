import numpy as np
soma=0
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

for i in matriz:
  soma+=i

print(soma)