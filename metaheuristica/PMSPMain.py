import random
import numpy as np

from PMSPSolution import PMSPSolution
from PMSPRestrictions import PMSPRestrictions


if __name__ == '__main__':
    random.seed()
    '''
     VAI LER DO ARQUIVO:
     id
     numero de máquinas
     numero de jobs
     
     P_1_1 P_1_2 ... P_1_m : processamento do job 1 nas máquinas de 1 até m
     P_2_1 P_2_2 ... P_2_m : processamento do job 2 nas máquinas de 1 até m
     ...
     P_N_1 P_N_2... P_N_M  : processamento do job n nas máquinas de 1 até m
    
     M matrizes com tempo de setup (uma matriz pra cada máquina)
    
     S_1_1_1  S_1_2_1 ... S_1_N_1
    ...
     S_N_1_1 S_N_2_1 ... S_N_N_1
    
     ...
     
     S_1_1_M S_1_2_M ... S_1_N_M
     ...
     S_N_1_M S_N_2_M ... S_N_N_M
    '''
    G = np.asarray(
    [ [
      [ 5,  5],
      [10, 10],
      [40, 20],
      [40, 20],  # matriz de Processamento   
      ],
     
      [
      [ 0,  1,  2,  3],     # matriz de setup pra máquina 1
      [ 6,  0,  5,  4],       
      [ 7,  8,  0,  9],
      [10, 11, 12,  0]
      ],

      [
      [ 0, 13, 14, 15],    # matriz de setup pra máquina 2
      [18,  0, 17, 16],       
      [19, 20,  0, 21],
      [22, 23, 24,  0]
      ]
    ])     
    
    restrictions = PMSPRestrictions(2, 4, G) # 2 máquinas 4 jobs
   
    solution = PMSPSolution.random_instance(2, 4, restrictions)
    if solution.fitness == -1:
        solution.fitness = restrictions.evaluate(solution)
    print('solution: ', solution.order_of_tasks)
    print('solution fitness: %d' % solution.fitness)
   
    newSol = PMSPSolution.create_instance(2, 4, restrictions, [[2,1],[3,0]])
    print('new sol: ', newSol.order_of_tasks)
    print('newSol fitness: ', newSol.fitness)

