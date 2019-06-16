import numpy as np


class PMSPInstance:
    def __init__(self,
                 m : int,
                 n : int):
        self.m = m
        self.n = n

        self.x = np.zeros((n+1, n+1, m), dtype=bool)

    def from_order(self,
                   order : np.ndarray):
        pass

    def to_order(self):
        pass           
