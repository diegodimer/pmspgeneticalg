import math
import numpy as np

from PMSPInstance import PMSPInstance


class PMSPRestrictions:
    def __init__(self,
                 G : np.ndarray):
        self.G = G.copy()

    def is_valid(self,
                 instance : PMSPInstance):
        return True


if __name__ == '__main__':
    restrictions = PMSPRestrictions(np.ndarray((1, 1)))
    instance = PMSPInstance(2, 2)
    if restrictions.is_valid(instance):
        print('Valid instance!')
    else:
        print('Invalid instance!')

    instance.x[0, 0, 1] = True
    print(instance.x[0, 0, 0] * 100)
    print(instance.x[0, 0, 1] * 100)
