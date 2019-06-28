import random
import numpy as np
import Operators as OP
from PMSPSolution import PMSPSolution
from PMSPRestrictions import PMSPRestrictions
from GeneticAlgorithm import GeneticAlgorithm

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
#    G = np.asarray(
#    [ [
#      [ 5,  5],
#      [10, 10],
#      [40, 20],
#      [40, 20],  # matriz de Processamento   
#      ],
#     
#      [
#      [ 0,  1,  2,  3],     # matriz de setup pra máquina 1
#      [ 6,  0,  5,  4],       
#      [ 7,  8,  0,  9],
#      [10, 11, 12,  0]
#      ],
#
#      [
#      [ 0, 13, 14, 15],    # matriz de setup pra máquina 2
#      [18,  0, 17, 16],       
#      [19, 20,  0, 21],
#      [22, 23, 24,  0]
#      ]
#    ])     
    G = np.asarray(
    [ 
     [ [5, 5],
       [10, 10],
       [40, 20],
       [40, 20]
      ],
     
     [ [0, 15, 13, 11],
       [18, 0, 12, 10],
       [15, 7, 0, 5],
       [14, 8, 5, 1]
     ],
     
     [ [0, 11, 10, 31],
       [20, 0, 24, 22],
       [7, 1, 0, 10],
       [6, 5, 4, 0]
     ]
    ])
    
    restrictions = PMSPRestrictions(2, 4, G) # 2 máquinas 4 jobs
   
    solution = PMSPSolution.random_instance(restrictions)
    if solution.fitness == -1:
        solution.fitness = restrictions.evaluate(solution)
    
    newSol = PMSPSolution.create_instance(restrictions, [[0,1],[3,2]])
    restrictions.evaluate_machine(newSol, 0)
    op = OP.Operators(newSol.restrictions)
#    newnew = op.firstCrossOver(newSol, solution)
    print('pais: ', solution.order_of_tasks, 'fitness: ', solution.fitness)
    newnew = op.onePointMutation(solution, 1)

#    print('pais: ',newSol.order_of_tasks, 'fitness: ', newSol.fitness)
    print('filho: ',newnew.order_of_tasks, 'fitness: ', newnew.fitness)
    GA = GeneticAlgorithm(restrictions)
    GA.run(1060)
#   