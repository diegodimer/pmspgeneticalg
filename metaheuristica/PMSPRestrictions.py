import numpy as np

from PMSPSolution import PMSPSolution


class PMSPRestrictions:
    def __init__(self,
                 G : np.ndarray):
        self.G = G.copy()

    def is_valid(self,
                 instance : PMSPSolution):
        return True


