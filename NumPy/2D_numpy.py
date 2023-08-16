import numpy as np

# Geração de dados 2D com numpy
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)

weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))

print(np_city)
print(np.mean(np_city[:,0]))
