import random
import numpy as np

from PMSPSolution import PMSPSolution
from PMSPRestrictions import PMSPRestrictions


if __name__ == '__main__':
    random.seed()
    
    G = np.asarray(
      # Being the first to execute
    [[[0, 0],       # Don't care
      [9999, 4182], # Task 0
      [200, 42]],   # Task 1
     
      # Executing after task 0
      [[0, 0],      # Don't care
      [0, 0],       # Task 0
      [2500, 1000]],# Task 1

      # Executing after task 1
      [[0, 0],      # Don't care
      [20, 12],     # Task 0
      [0, 0]]])     # Task 1
    restrictions = PMSPRestrictions(2, 2, G)
    solution = PMSPSolution.random_instance(2, 2, restrictions)
    
    print("Order:")
    print(solution.to_order())
    
    if restrictions.check_validity(solution.to_order()):
        print('Valid instance! Fitness: %d' % restrictions.evaluate(solution.x))
    else:
        print('Invalid instance!')
    
    
    # solution.x[0, 0, 1] = True
    # print(solution.x[0, 0, 0] * 100)
    # print(solution.x[0, 0, 1] * 100)
    
