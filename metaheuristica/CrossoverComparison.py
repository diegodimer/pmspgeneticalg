import random
import copy

from PMSPSolution import PMSPSolution
from PMSPRestrictions import PMSPRestrictions
from Operators import Operators
from PMSPMain import ler_instancia


if __name__ == '__main__':
    random.seed()
    G2 = ler_instancia("20on4Rp50Rs50_1original.dat")
    restrictions = PMSPRestrictions(len(G2[0][0]),len(G2[0]), G2)
    operators = Operators(restrictions)

    solution_a = PMSPSolution.random_instance(restrictions)
    solution_b = PMSPSolution.random_instance(restrictions)
    print('M = ', restrictions.m, 'N = ', restrictions.n)
    print('========================')
    print('Initial fitness: ', solution_a.fitness)
    print('Initial fitness: ', solution_b.fitness)
    print('========================')
    relinked = operators.path_relinking(copy.deepcopy(solution_a), copy.deepcopy(solution_b))
    first = operators.firstCrossOver(copy.deepcopy(solution_a), copy.deepcopy(solution_b))
    vallada1, vallada2 = operators.crossOver_Vallada(copy.deepcopy(solution_a), copy.deepcopy(solution_b))
    vallada_ls1, vallada_ls2 = operators.crossOver_Vallada_LocalSearch(copy.deepcopy(solution_a), copy.deepcopy(solution_b))
    print('Relinked: ', relinked.fitness)
    print('First: ', first.fitness)
    print('Vallada: ', min(vallada1.fitness, vallada2.fitness))
    print('Vallada with Local Search: ', min(vallada_ls1.fitness, vallada_ls2.fitness))
