import random
import numpy as np

from PMSPSolution import PMSPSolution
from PMSPRestrictions import PMSPRestrictions


if __name__ == '__main__':
    random.seed()
    restrictions = PMSPRestrictions(np.ndarray((1, 1)))
    instance = PMSPSolution.random_instance(5, 20)
    if restrictions.is_valid(instance):
        print('Valid instance!')
    else:
        print('Invalid instance!')

    instance.x[0, 0, 1] = True
    print(instance.x[0, 0, 0] * 100)
    print(instance.x[0, 0, 1] * 100)
