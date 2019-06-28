import random
import math
import PMSPRestrictions
from PMSPSolution import PMSPSolution
import numpy as numpy
class Operators:
    def __init__(self, 
                 restrictions: PMSPRestrictions):
        self.restrictions = restrictions
        

    # Adds a value between (-1.0, 1.0) / self.scale to one weight
    def onePointMutation(self, 
                         solution: PMSPSolution, 
                         mutationScale):
    
        newSolution = solution.order_of_tasks
        firstMachine = random.randint(0, self.restrictions.m-1)
        secondMachine = random.randint(0, self.restrictions.m-1)
        firstTask = random.randint(0, len(newSolution[firstMachine])-1) if len(newSolution[firstMachine])>0 else -1
        secondTask = random.randint(0, len(newSolution[secondMachine])-1) if len(newSolution[secondMachine])>0 else -1
        
        if firstTask != -1 and secondTask != -1:
            newSolution[firstMachine][firstTask], newSolution[secondMachine][secondTask] = newSolution[secondMachine][secondTask], newSolution[firstMachine][firstTask]  
        elif firstTask == -1 and secondTask != -1:
            newSolution[firstMachine].append(newSolution[secondMachine][secondTask])
            newSolution[secondMachine].pop(newSolution[secondMachine].index(newSolution[secondMachine][secondTask]))
        elif secondTask == -1 and firstTask != -1:
            newSolution[secondMachine].append(newSolution[firstMachine][firstTask])
            newSolution[firstMachine].pop(newSolution[firstMachine].index(newSolution[firstMachine][firstTask]))

        solution.order_of_tasks = newSolution
        solution.restrictions.evaluate_machine(solution, firstMachine)
        solution.restrictions.evaluate_machine(solution, secondMachine)
        return solution
#        if random.random() < mutationScale :
#			#PICKS TASK RANDOMLY TO BE REMOVED FROM A MACHINE
#            while True:
#                maquina_sorteada = random.randrange(0,solution.m)
#                if len(solution.order_of_tasks[maquina_sorteada]) != 0:
#                    break
#                tarefa_sorteada = random.randrange(0,len(solution.order_of_tasks[maquina_sorteada]))
#                auxiliar = solution.order_of_tasks[maquina_sorteada][tarefa_sorteada]
#                del solution.order_of_tasks[maquina_sorteada][tarefa_sorteada]
#		
#			#CHOOSES NEW MACHINE AND INDEX (DIFFERENT FROM THE ORIGINAL) TO PUT THE CHOSEN TASK
#            while True:
#                maquina_sorteada2 = random.randrange(0,solution.m)
#                if len(solution.order_of_tasks[maquina_sorteada2]) == 0:
#                    tarefa_sorteada2 = 0
#                else: tarefa_sorteada2 = random.randrange(0,len(solution.order_of_tasks[maquina_sorteada2]))
#                if not(maquina_sorteada == maquina_sorteada2 and tarefa_sorteada == tarefa_sorteada2):
#                    break
#                solution.order_of_tasks[maquina_sorteada2].insert(tarefa_sorteada2,auxiliar)
#            return solution

    # Adds a value between (-1.0, 1.0) / self.scale to each weight
    def allPointsMutation(self, 
                          solution: PMSPSolution, 
                          mutationScale):
        m=0
        for i in solution.order_of_tasks:
            if random.random() < 0.20: # com 20% de chances 
                random.shuffle(i) #aleatoriza a ordem das tarefas naquela máquina
                solution.restrictions.evaluate_machine(solution, m) #recalcula o fitness da solução praquela máquina
        return solution

    # Returns the mean of the two solutions
    def firstCrossOver(self, 
                      solution1: PMSPSolution, 
                      solution2: PMSPSolution):
        restrictions = self.restrictions
        m = self.restrictions.m
        n = self.restrictions.n
        newSolution = [[] for x in range(m)] 
        jobs = [x for x in range(n)]

        for i in range(m): #pra cada máquina
            if solution1.c[i] < solution2.c[i]: #poem a linha do pai com menor makespan
                for j in solution1.order_of_tasks[i]:
                    if j not in sum(newSolution, []):
                        newSolution[i].append(j)
                        jobs.pop(jobs.index(j))
            else:
                for j in solution2.order_of_tasks[i]:
                    if j not in sum(newSolution, []):
                        newSolution[i].append(j)
                        jobs.pop(jobs.index(j))
    
        sol = PMSPSolution(m,n,restrictions, newSolution)
        while len(jobs) != 0: #poem os jobs restantes nas máquinas com menor makespan (tentar não piorar uma solução)
            minMachine= 0
            minValue  = restrictions.evaluate_machine(sol,0)
            for i in range(1,m-1):
                newValue = restrictions.evaluate_machine(sol,i)
                if newValue < minValue:
                    minValue = newValue
                    minMachine = i
            newJob = jobs.pop()
            newSolution[minMachine].append(newJob)
       
        sol = PMSPSolution.create_instance(solution1.restrictions, newSolution)
        return sol
            
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