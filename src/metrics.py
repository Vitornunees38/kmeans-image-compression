import numpy as np

def calcular_mse(original, comprimida):
    return np.mean((original*255 - comprimida*255) ** 2)