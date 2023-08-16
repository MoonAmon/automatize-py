import numpy as np

matrizA = np.random.randint(0, 100, size=(5, 2))
matrizB = np.random.randint(0, 100, size=(5, 2))

matrizC = np.array(matrizA) + np.array(matrizB)


print(matrizA[0][1])
