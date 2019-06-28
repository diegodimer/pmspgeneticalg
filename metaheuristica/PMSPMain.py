import random
import numpy as np
import math
from PMSPSolution import PMSPSolution
from PMSPRestrictions import PMSPRestrictions
from Operators import Operators
import GeneticAlgorithm

def ler_instancia(nome):
        f = open(nome,"r")
        if f.mode == "r":
                contents = f.readlines()
                print(contents[1])
                print(contents[2])
                print(contents[4])
                linha = contents[4].split(" ")
        f.close()
        G = []
		
		
		# writes G[0], matrix with processing times
        line=4
        matriz_0 = []
        for i in range(int(contents[2])):
            jobs = contents[line].split(" ")
            line = line + 1
            aux0 = []
            for j in range(int(contents[1])):
                aux0.append(int(jobs[j]))
            #print(aux0)
            matriz_0.append(aux0)
        #print(matriz_0)
        G.append(matriz_0)
		
		#writes on G[1] ... G[n-1] matrix with setup times
        for i in range(int(contents[1])):
            line = line + 1
            matriz_s = []
            for j in range(int(contents[2])):
			    #print(contents[line])
                jobs_after = contents[line].split(" ")
                line = line + 1
                aux1 = []
                for k in range(int(contents[2])):
                    aux1.append(int(jobs_after[k]))
                matriz_s.append(aux1)
            #print("matriz_s: ")
            #print(matriz_s)
            G.append(matriz_s)
			
		
        return G

def main():
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

    
    G2 = ler_instancia("20on4Rp50Rs50_1original.dat")
    print("valor de G[0]: ")
    print(G2[0])
    print("valor de g[1]: ")
    print(G2[1])
    print("valor de len(G2[0][0]): ")
    print(str(len(G2[0][0])))
    print("valor de len(G2[0]): ")
    print(str(len(G2[0])))
    restrictions = PMSPRestrictions(len(G2[0][0]),len(G2[0]), G2)

    
   # restrictions = PMSPRestrictions(2, 4, G) # 2 máquinas 4 jobs

    solution1 = PMSPSolution.random_instance(restrictions)
    print('solution: ', solution1.order_of_tasks)

    solution2 = PMSPSolution.random_instance(restrictions)
    print('solution: ', solution2.order_of_tasks)

    operators = Operators(restrictions)
    operators.crossOver_Vallada_LocalSearch(solution1,solution2)
#    if solution.fitness == -1:
#        solution.fitness = restrictions.evaluate(solution)
#    print('solution: ', solution.order_of_tasks)
#    print('solution fitness: %d' % solution.fitness)

#    newSol = PMSPSolution.create_instance(restrictions, [[2,1],[0,3]])
#    print('new sol: ', newSol.order_of_tasks)
#    print('newSol fitness: ', newSol.fitness)
#    print('newSol c: ', newSol.c)
#    restrictions.evaluate_machine(newSol, 0)
#    ga = GeneticAlgorithm.GeneticAlgorithm(restrictions)
#    ga.run(100)
 #   newSol.order_of_tasks = [[0,1,2],[]]
 #   operators = Operators(restrictions)
 #   operators.local_search(restrictions, newSol.order_of_tasks[0],0,3)
 #   newSol2 = PMSPSolution.create_instance(restrictions, [[0,1,2,3],[]])
 #   newSol.order_of_tasks = [[0],[3,2,1]]
 #   operators.crossOver_Vallada_LocalSearch(newSol2,newSol)
                                    
    
if __name__ == '__main__':
    main()

