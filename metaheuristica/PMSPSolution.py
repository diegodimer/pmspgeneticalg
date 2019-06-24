import numpy as np
import random

import PMSPRestrictions


class PMSPSolution:
    def __init__(self,
                 m : int,
                 n : int,
                 restrictions : PMSPRestrictions):
        self.m = m
        self.n = n
        self.restrictions = restrictions
        
 

    @staticmethod
    def random_instance(m : int,
                        n : int,
                        restrictions : PMSPRestrictions):
        # Randomizing the machines, so the first ones aren't favored
        machines = list(range(m))
        random.shuffle(machines)
        
        # Initializes with zero task for each machine
        tasks_per_machine = [0] * m

        # Randomizes the number of tasks for each machine
        tasks_left = n
        for machine in machines:
            ntasks = random.randint(0, tasks_left)
            tasks_per_machine[machine] = ntasks
            tasks_left -= ntasks
            
        # Adding the remaining tasks to the last machine
        tasks_per_machine[m-1] += tasks_left

        # Randomizes the tasks for each machine
        order_of_tasks = []
        tasks = list(range(n))
        random.shuffle(tasks)

        for no_tasks in tasks_per_machine:
            mtasks = []
            for i in range(no_tasks):
                mtasks.append(tasks.pop())
            order_of_tasks.append(mtasks)

        # Generating the instance
        instance = PMSPSolution(m, n, restrictions)
        instance.order_of_tasks = order_of_tasks
        instance.fitness = restrictions.evaluate(instance)
        return instance
    
    @staticmethod
    def create_instance(m : int,
                        n : int,
                        restrictions : PMSPRestrictions,
                        order_of_tasks: list):
        instance = PMSPSolution(m, n, restrictions)
        instance.order_of_tasks = order_of_tasks
        if(restrictions.check_validity(instance)):
            instance.fitness = restrictions.evaluate(instance)
            return instance
        else:
            raise Exception("Instancia inválida")
        
        
