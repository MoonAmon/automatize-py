import numpy as np

x = np.round(np.random.normal(1.75, 0.20, 5000), 2)

y = np.round(np.random.normal(60.32, 15, 5000), 2)

matriz = np.column_stack((y, x))

print(matriz)