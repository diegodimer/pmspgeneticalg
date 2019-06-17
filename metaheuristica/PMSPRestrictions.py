import numpy as np


class PMSPRestrictions:
    def __init__(self,
                 m : int,
                 n : int,
                 G : np.ndarray):
        self.m = m
        self.n = n
        self.G = G.copy()

    def check_validity(self,
                       order : list):
        """for l in order:
            print(l)"""
                   
        total_machines = len(order)
        total_tasks = 0
        for machine_order in order:
            total_tasks += len(machine_order)
            
        # print(self.x.shape)
        # print((total_tasks + 1, total_tasks + 1, total_machines))
        
        assert (self.G.shape == (total_tasks + 1, total_tasks + 1, total_machines)), \
               "Wrong number of tasks/machines"
               
        tasks = [0] * self.n
        
        for machine_order in order:
            for t in machine_order:
                assert (tasks[t] == 0), "Task %d assigned twice" % t
                tasks[t] = 1


