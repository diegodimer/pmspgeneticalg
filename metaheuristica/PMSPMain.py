import random
import numpy as np

from PMSPSolution import PMSPSolution
from PMSPRestrictions import PMSPRestrictions


if __name__ == '__main__':
    random.seed()
    restrictions = PMSPRestrictions(5, 20, np.ndarray((21, 21, 5)))
    solution = PMSPSolution.random_instance(5, 20, restrictions)
    
    print("After:")
    print(solution.to_order())
    
    
    if restrictions.check_validity(solution.to_order()):
        print('Valid instance!')
    else:
        print('Invalid instance!')
    
    
    solution.x[0, 0, 1] = True
    print(solution.x[0, 0, 0] * 100)
    print(solution.x[0, 0, 1] * 100)
