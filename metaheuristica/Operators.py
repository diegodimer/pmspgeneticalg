import random
import math
import copy
import PMSPRestrictions
from PMSPSolution import PMSPSolution
import numpy as np
import sys


class Operators:
    def __init__(self,
                 restrictions: PMSPRestrictions):
        self.restrictions = restrictions



    def onePointMutation(self,
                         solution: PMSPSolution):

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



    def allPointsMutation(self,
                          solution: PMSPSolution):
        m=0
        for i in solution.order_of_tasks:
            if random.random() < 0.20: # com 20% de chances
                random.shuffle(i) #aleatoriza a ordem das tarefas naquela máquina
                solution.restrictions.evaluate_machine(solution, m) #recalcula o fitness da solução praquela máquina
            m+=1
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

        offspring = []
        offspring.append(PMSPSolution.create_instance(self.restrictions, list1))
        offspring.append(PMSPSolution.create_instance(self.restrictions, list2))

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
#        print(jobs_list1)
#        print(jobs_list2)
#        print(list1)
#        print(list2)
        offspring = []
        offspring.append(PMSPSolution.create_instance(self.restrictions, list1))
        offspring.append(PMSPSolution.create_instance(self.restrictions, list2))
        return offspring

    def local_search(self,restrictions: PMSPRestrictions, solution: [],machine: int,job: int):
#        print(solution)

        if len(solution) > 0 :
            min_setup = sys.maxsize;
            for j in range(len(solution)+1):
                if j == len(solution):
                    setup = restrictions.G[machine+1][solution[j-1]][job]
                elif j == 0:
                    setup = restrictions.G[machine+1][job][solution[0]]
                else:
                    setup = restrictions.G[machine+1][job][solution[j]]
                    setup += restrictions.G[machine+1][solution[j-1]][job]
                    setup -= restrictions.G[machine+1][solution[j-1]][solution[j]]

#                print("valor do setup: "+str(setup)+" para j = "+str(j))
                if setup < min_setup:
#                    print(" atualizando setup, novo valor: "+str(setup)+" \n")
                    min_setup = setup
                    fitness_index = j
#            print("melhor index pra tarefa "+str(job)+" eh o index "+str(fitness_index)+" \n")

		#IF FITNESS_INDEX IS EQUAL TO THE LIST SIZE, IT MEANS THAT THE JOB MUST BE APPENDED AT THE END
            return fitness_index
        else: return 0

    def path_relinking(self, guiding: PMSPSolution, initiating: PMSPSolution):
        solutions = []
        middle_solution = copy.deepcopy(initiating)
        best_solution = np.asarray(np.copy(middle_solution.order_of_tasks))
        best_fitness = initiating.fitness

        # For each task in the guiding solution
        for machine_g in range(len(guiding.order_of_tasks)):
            for task_g in range(len(guiding.order_of_tasks[machine_g])):
                j = (machine_g, task_g)
                k = None

                # Searches for the task in the initiating solution
                for machine_i in range(len(middle_solution.order_of_tasks)):
                    if k is not None:
                        break

                    for task_i in range(len(middle_solution.order_of_tasks[machine_i])):
                        if guiding.order_of_tasks[machine_g][task_g] == middle_solution.order_of_tasks[machine_i][task_i]:
                            # Guiding task found on initiating solution
                            k = (machine_i, task_i)
                            break

                if k is None:
                    raise Exception("Instancia invalida!")

                if k == j:
                    # Task already on the right position
                    continue

                if len(middle_solution.order_of_tasks[machine_g]) > task_g:
                    # There is enough tasks on initiating's machine_g to be
                    # moved to k
                    t_k = middle_solution.order_of_tasks[k[0]][k[1]]
                    t_j = middle_solution.order_of_tasks[j[0]][j[1]]
                    middle_solution.order_of_tasks[k[0]][k[1]] = t_j
                    middle_solution.order_of_tasks[j[0]][j[1]] = t_k
                else:
                    # Not enough tasks; we will just remove from k and insert
                    # at the end of machine_g (both on initiating)
                    t_k = middle_solution.order_of_tasks[k[0]].pop(k[1])
                    middle_solution.order_of_tasks[machine_g].append(t_k)

                # Updating the fitness
                if k[0] == j[0]:
                    # Swapped tasks are on the same machine
                    self.restrictions.evaluate_machine(middle_solution, k[0])
                    middle_solution.fitness = max(middle_solution.c)
                else:
                    # Two different machines
                    self.restrictions.evaluate_machine(middle_solution, k[0])
                    self.restrictions.evaluate_machine(middle_solution, j[0])
                    middle_solution.fitness = max(middle_solution.c)

                # Updating best solution
                if middle_solution.fitness < best_fitness:
                    best_solution = np.asarray(copy.deepcopy(middle_solution.order_of_tasks))
                    best_fitness = middle_solution.fitness

        return PMSPSolution.create_instance(self.restrictions, best_solution.tolist())
