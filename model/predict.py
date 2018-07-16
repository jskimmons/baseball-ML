import pandas as pd
import numpy as np

import dill as pickle

class Model:

    def __init__(self):
        filename = 'model_v1.pk'

        with open(filename ,'rb') as f:
            self.loaded_model = pickle.load(f)


if __name__ == '__main__':

    filename = 'model_v1.pk'

    with open(filename ,'rb') as f:
        loaded_model = pickle.load(f)

    li = [0.257, 0.182, 0.308, 0.250, 0.679, 0.614, 0.371, 0.364, 3.00, 5.0] # 1
    li2 = [0.176,0.219,0.2,0.265,0.465,0.546,0.265,0.281,0.0,3.0] # 1
    li3 = [0.156,0.2,0.208,0.25,0.431,0.472,0.222,0.222,0.75,0.0] # 0

    testLi = [0.235, 0.233, 0.333, 0.303, 0.598, 0.736, 0.265, 0.433, 6.75, 4.00]

    a = np.reshape(li, (1, -1))
    b = np.reshape(li2, (1, -1))
    c = np.reshape(li3, (1, -1))
    test = np.reshape(testLi, (1, -1))

    print(loaded_model.predict(a))
    print(loaded_model.predict(b))
    print(loaded_model.predict(c))
    print(loaded_model.predict(test))