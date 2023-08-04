import numpy as np


def mkmatriz2d(contX, contY):
    x = np.round(np.random.normal(1.75, 0.20, contX), 2)

    y = np.round(np.random.normal(60.32, 15, contY), 2)

    matriz = np.column_stack((x, y))

    return matriz
