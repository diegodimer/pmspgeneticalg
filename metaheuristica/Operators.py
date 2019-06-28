import random
import math
import PMSPRestrictions
import PMSPSolution

class Operators:
    def __init__(self, 
                 restrictions: PMSPRestrictions):
        self.restrictions = restrictions
        

    # Adds a value between (-1.0, 1.0) / self.scale to one weight
    def onePointMutation(self, 
                         solution: PMSPSolution, 
                         mutationScale):
        if random.random() < mutationScale :
			#PICKS TASK RANDOMLY TO BE REMOVED FROM A MACHINE
            while True:
                maquina_sorteada = random.randrange(0,solution.m)
                if len(solution.order_of_tasks[maquina_sorteada]) != 0:
                    break
                tarefa_sorteada = random.randrange(0,len(solution.order_of_tasks[maquina_sorteada]))
                auxiliar = solution.order_of_tasks[maquina_sorteada][tarefa_sorteada]
                del solution.order_of_tasks[maquina_sorteada][tarefa_sorteada]
		
			#CHOOSES NEW MACHINE AND INDEX (DIFFERENT FROM THE ORIGINAL) TO PUT THE CHOSEN TASK
            while True:
                maquina_sorteada2 = random.randrange(0,solution.m)
                if len(solution.order_of_tasks[maquina_sorteada2]) == 0:
                    tarefa_sorteada2 = 0
                else: tarefa_sorteada2 = random.randrange(0,len(solution.order_of_tasks[maquina_sorteada2]))
                if not(maquina_sorteada == maquina_sorteada2 and tarefa_sorteada == tarefa_sorteada2):
                    break
                solution.order_of_tasks[maquina_sorteada2].insert(tarefa_sorteada2,auxiliar)
            return solution

    # Adds a value between (-1.0, 1.0) / self.scale to each weight
    def allPointsMutation(self, 
                          solution: PMSPSolution, 
                          mutationScale):
#      newSolution = []
#      for i in range(self.numberOfWeights):
#        newSolution.append(solution[i] + (random.uniform(-1.0, 1.0) / mutationScale))
#      return newSolution
        raise NotImplemented

    # Returns the mean of the two solutions
    def meanCrossOver(self, 
                      solution1: PMSPSolution, 
                      solution2: PMSPSolution):
#      newSolution = []
#      for i in range(len(solution1)):
#        newValue = (solution1[i] + solution2[i]) / 2.0
#        newSolution.append(newValue)
#      return newSolution
        raise NotImplemented

    def crossOver_Vallada(self, parent1: PMSPSolution, parent2: PMSPSolution):
        	
        list1 = []
        list2 = []
        jobs_list1 = set()
        jobs_list2 = set()
        # populates set of offspring 1 and 2 with their jobs from first parent
        for machine in range(parent1.m):
            mean_index = math.floor(len(parent1.order_of_tasks[machine])/2)
            for i in range(mean_index):
                jobs_list1.add(parent1.order_of_tasks[machine][i])
            for i in range(mean_index,len(parent1.order_of_tasks[machine])):
                jobs_list2.add(parent1.order_of_tasks[machine][i])
			
		
        for machine in range(parent1.m):
            mean_index = math.floor(len(parent1.order_of_tasks[machine])/2)
            aux1=[]
            #jobs from the first position to the mean position are copied to the first offspring
            for i in range(mean_index):
                aux1.append(parent1.order_of_tasks[machine][i])
	
            #jobs from the mean + 1 to the end are copied to the second offspring
            aux2 = []
            for i in range(mean_index,len(parent1.order_of_tasks[machine])):
                aux2.append(parent1.order_of_tasks[machine][i])
				
			# jobs from the parent 2 which are not already in the offspring are inserted in the same order
            for i in range(len(parent2.order_of_tasks[machine])):
                if parent2.order_of_tasks[machine][i] not in jobs_list1:
                    aux1.append(parent2.order_of_tasks[machine][i])
                    jobs_list1.add(parent2.order_of_tasks[machine][i])
                if parent2.order_of_tasks[machine][i] not in jobs_list2:
                    aux2.append(parent2.order_of_tasks[machine][i])
                    jobs_list2.add(parent2.order_of_tasks[machine][i])
			
            list1.append(aux1)
            list2.append(aux2)
        print(jobs_list1)
        print(jobs_list2)
        print(list1)
        print(list2)	
        offspring = []
        offspring.append(list1)
        offspring.append(list2)
        
        return offspring
		
    def crossOver_Vallada_LocalSearch(self, parent1: PMSPSolution, parent2: PMSPSolution):
        list1 = []
        list2 = []
        jobs_list1 = set()
        jobs_list2 = set()
        # populates set of offspring 1 and 2 with their jobs from first parent
        for machine in range(parent1.m):
            mean_index = math.floor(len(parent1.order_of_tasks[machine])/2)
            for i in range(mean_index):
                jobs_list1.add(parent1.order_of_tasks[machine][i])
            for i in range(mean_index,len(parent1.order_of_tasks[machine])):
                jobs_list2.add(parent1.order_of_tasks[machine][i])
			
		
        for machine in range(parent1.m):
            mean_index = math.floor(len(parent1.order_of_tasks[machine])/2)
            aux1=[]
            #jobs from the first position to the mean position are copied to the first offspring
            for i in range(mean_index):
                aux1.append(parent1.order_of_tasks[machine][i])
	
            #jobs from the mean + 1 to the end are copied to the second offspring
            aux2 = []
            for i in range(mean_index,len(parent1.order_of_tasks[machine])):
                aux2.append(parent1.order_of_tasks[machine][i])
				
			# jobs from the parent 2 which are not already in the offspring are inserted in the same order
            for i in range(len(parent2.order_of_tasks[machine])):
                if parent2.order_of_tasks[machine][i] not in jobs_list1:
                    best_index = self.local_search(self.restrictions,aux1,machine,parent2.order_of_tasks[machine][i])
                    if best_index == len(aux1):
                        aux1.append(parent2.order_of_tasks[machine][i])
                    else: aux1.insert(best_index,parent2.order_of_tasks[machine][i])
					
                    jobs_list1.add(parent2.order_of_tasks[machine][i])
					
                if parent2.order_of_tasks[machine][i] not in jobs_list2:
                    best_index = self.local_search(self.restrictions,aux2,machine,parent2.order_of_tasks[machine][i])
                    if best_index == len(aux2):
                        aux2.append(parent2.order_of_tasks[machine][i])
                    else: aux2.insert(best_index,parent2.order_of_tasks[machine][i])	
					
                    jobs_list2.add(parent2.order_of_tasks[machine][i])
			
            list1.append(aux1)
            list2.append(aux2)
        print(parent1.order_of_tasks)
        print(parent2.order_of_tasks)
        print(list1)
        print(list2)	
        offspring = []
        offspring.append(list1)
        offspring.append(list2)
			

    def local_search(self,restrictions: PMSPRestrictions, solution: [],machine: int,job: int):
        print(solution)
        if len(solution) > 0 :
            min_setup = 999999
            for j in range(len(solution)+1):
                if j == len(solution):
                    setup = restrictions.G[machine+1][solution[j-1]][job]
                elif j == 0:
                    setup = restrictions.G[machine+1][job][solution[0]]
                else: 
                    setup = restrictions.G[machine+1][job][solution[j]]
                    setup += restrictions.G[machine+1][solution[j-1]][job]
                    setup -= restrictions.G[machine+1][solution[j-1]][solution[j]]
                #print("valor do setup: "+str(setup)+" para j = "+str(j))
                if setup < min_setup:
                    #print(" atualizando setup, novo valor: "+str(setup)+" \n")
                    min_setup = setup
                    fitness_index = j
            #print("melhor index pra tarefa "+str(job)+" eh o index "+str(fitness_index)+" \n")
		#IF FITNESS_INDEX IS EQUAL TO THE LIST SIZE, IT MEANS THAT THE JOB MUST BE APPENDED AT THE END
            return fitness_index
        else: return 0

    # newSolution takes the first half of the weights from solution1 and the other half from solution2
    def mediumPointCrossOver(self, 
                             solution1: PMSPRestrictions, 
                             solution2: PMSPRestrictions):
#      newSolution = []
#      for i in range(len(solution1)):
#        if i < len(solution1) / 2:
#          newSolution.append(solution1[i])
#        else:
#          newSolution.append(solution2[i])
#      return newSolution
        raise NotImplemented