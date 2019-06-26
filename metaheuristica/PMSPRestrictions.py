import numpy as np
import PMSPSolution

class PMSPRestrictions:
    def __init__(self,
                 m : int,
                 n : int,
                 G : np.ndarray):
        self.m = m
        self.n = n
        self.G = G.copy()

    def evaluate(self,
                 solution: PMSPSolution):
        max_c = 0       

        c = [0] * self.m
        for i in range(self.m):
            current = 0
            for j in solution.order_of_tasks[i]:
                # i+1 pq a matriz 0 e a de processamento, current é a atual, current-1 é a anterior
                setup_time = self.G[i+1][solution.order_of_tasks[i][current-1]][solution.order_of_tasks[i][current]] if current != 0 else 0
                current+=1
                processing_time = self.G[0][j][i]
                c[i] += setup_time + processing_time
        max_c = max(c)
        solution.c = c #salva a solução pra cada maquina
        return max_c
    
    def evaluate_machine(self,
                         solution: PMSPSolution,
                         machine: int):
        newC = 0
        current = 0
        for j in solution.order_of_tasks[machine]:
            setup_time = self.G[machine+1][solution.order_of_tasks[machine][current-1]][solution.order_of_tasks[machine][current]] if current != 0 else 0
            current+=1
            processing_time = self.G[0][j][machine]
            newC += setup_time + processing_time
        solution.c[machine] = newC
        solution.fitness = max(solution.c)

        
    def check_validity(self,
                       solution : PMSPSolution):
        if len(solution.order_of_tasks) == self.m: # se tem uma linha pra cada máquina mesmo
            if len(np.concatenate(solution.order_of_tasks)) == self.n: # se tem o numero certo de tarefas
                if len(np.unique(np.concatenate(solution.order_of_tasks))) == len(np.concatenate(solution.order_of_tasks)):
                    return True # se nenhuma tarefa foi associada 2 vezes
        return False

