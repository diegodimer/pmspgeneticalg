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
        print('SOLUCAO: ', solution.order_of_tasks)
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
                print('\n')
        print('c: ', c)
        max_c = max(c)
        return max_c
            

    def check_validity(self,
                       order : list):
        """for l in order:
            print(l)"""
                   
        total_machines = len(order)
        total_tasks = 0
        for machine_order in order:
            total_tasks += len(machine_order)
            
        # print(self.G.shape)
        # print((total_tasks + 1, total_tasks + 1, total_machines))
        
#        assert (self.G.shape == (total_tasks + 1, total_tasks + 1, total_machines)), \
#               "Wrong number of tasks/machines"
               
        tasks = [0] * self.n
        
        for machine_order in order:
            for t in machine_order:
                assert (tasks[t] == 0), "Task %d assigned twice" % t
                tasks[t] = 1

        return True

