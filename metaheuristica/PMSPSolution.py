import numpy as np
import random

from PMSPRestrictions import PMSPRestrictions


class PMSPSolution:
    def __init__(self,
                 m : int,
                 n : int,
                 restrictions : PMSPRestrictions):
        self.m = m
        self.n = n

        self.x = np.zeros((n+1, n+1, m), dtype=bool)
        self.restrictions = restrictions
        

    def from_order(self,
                   order : list):
        self.restrictions.check_validity(order)
        
        for i in range(self.m):
            machine_order = order[i]
            machine_total_tasks = len(machine_order)
            
            #print("MO", machine_order, machine_total_tasks)

            # Current machine has no tasks
            if machine_total_tasks == 0:
                continue
            
            # Dealing with extreme cases
            first_task = machine_order[0] + 1
            last_task = machine_order[machine_total_tasks-1] + 1
            
            self.x[0, first_task, i] = True
            self.x[last_task,  0, i] = True
            
            # Normal case will only happen when there's more than one task
            if machine_total_tasks == 1:
                continue
                
            previous_task = first_task
            for j in range(1, machine_total_tasks):
                current_task = machine_order[j] + 1
                self.x[previous_task, current_task, i] = True
                previous_task = current_task
                
            
    # Avoid using; (I think) it's really inefficient due to its complexity 
    # (would be something like O(mn²) if every machine could have every task)
    def to_order(self):
        order = []
        
        for i in range(self.m):
            machine_order = []
            
            previous_task = 0
            next_task = -1            
            
            while next_task != 0:
                next_task = -1
                
                # Searching for the next task
                for j in range(self.n + 1):
                    if self.x[previous_task, j, i]:
                        next_task = j
                        break
                
                # Next task was not found; no task for this machine
                if next_task == -1:
                    break

                if next_task != 0:
                    machine_order.append(next_task-1)
                                    
                previous_task = next_task
                
            order.append(machine_order)

        return order

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
        instance.from_order(order_of_tasks)
        instance.order_of_tasks = order_of_tasks
        return instance
