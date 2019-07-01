import sys
from PMSPRestrictions import PMSPRestrictions
import GeneticAlgorithm


def ler_instancia(nome):
        f = open(nome,"r")
        if f.mode == "r":
                contents = f.readlines()
#                print(contents[1])
#                print(contents[2])
#                print(contents[4])
#                linha = contents[4].split(" ")
        f.close()
        G = []
		
		
		# writes G[0], matrix with processing times
        line=4
        matriz_0 = []
        for i in range(int(contents[2])):
            jobs = contents[line].split(" ")
            line = line + 1
            aux0 = []
            for j in range(int(contents[1])):
                aux0.append(int(jobs[j]))
            #print(aux0)
            matriz_0.append(aux0)
        #print(matriz_0)
        G.append(matriz_0)
		
		#writes on G[1] ... G[n-1] matrix with setup times
        for i in range(int(contents[1])):
            line = line + 1
            matriz_s = []
            for j in range(int(contents[2])):
			    #print(contents[line])
                jobs_after = contents[line].split(" ")
                line = line + 1
                aux1 = []
                for k in range(int(contents[2])):
                    aux1.append(int(jobs_after[k]))
                matriz_s.append(aux1)
            #print("matriz_s: ")
            #print(matriz_s)
            G.append(matriz_s)
			
		
        return G

def main():
    try:
        G2 = ler_instancia(sys.argv[1])
        populationSize = int(sys.argv[2])
        maxIter = int(sys.argv[3])
        try:
            seed = int(sys.argv[4])
        except:
                seed = None
        restrictions = PMSPRestrictions(len(G2[0][0]),len(G2[0]), G2)
        ga = GeneticAlgorithm.GeneticAlgorithm(restrictions,populationSize,seed)
        pop = ga.run(maxIter)
        print("Best: ", pop.fitness, 'Solution: ', pop.order_of_tasks)
    except:
        print('Sintaxe invalida: python3 PMSPMain.py <arquivo de instancia> <tamanho da populacao> <max iteracoes> <seed/opcional>')
      

    
if __name__ == '__main__':
    main()

