import GeneticAlgorithm
import PMSPMain as main
from PMSPRestrictions import PMSPRestrictions


if __name__ == '__main__':
    G = main.ler_instancia("20on4Rp50Rs50_1original.dat")
    restrictions = PMSPRestrictions(len(G[0][0]),len(G[0]), G)
    ga = GeneticAlgorithm.GeneticAlgorithm(restrictions,1000)
    
    pop = ga.run(1000)

