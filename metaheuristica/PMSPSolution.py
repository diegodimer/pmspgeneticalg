import numpy as np
import random

class PMSPSolution:
    def __init__(self,
                 m : int,
                 n : int):
        self.m = m
        self.n = n

        self.x = np.zeros((n+1, n+1, m), dtype=bool)

    def from_order(self,
                   order : list):
        for l in order:
            print(l)

    def to_order(self):
        pass

    @staticmethod
    def random_instance(m : int,
                        n : int):
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
        instance = PMSPSolution(m, n)
        instance.from_order(order_of_tasks)

        return instance
