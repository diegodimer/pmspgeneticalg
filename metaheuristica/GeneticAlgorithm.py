import random
import math
from PMSPRestrictions import PMSPRestrictions
from PMSPSolution import PMSPSolution
from Operators import Operators


class GeneticAlgorithm:
    def __init__(self, 
                 restrictions: PMSPRestrictions, 
                 populationSize: int,
                 seed = None):
        self.m = restrictions.m
        self.n = restrictions.n
        self.restrictions = restrictions
        self.operators = Operators(restrictions)

        self.populationSize =   populationSize
        
        # Number of solutions generated per operator
        self.previousBestsSize = int(populationSize*0.1) # 10%
        self.onePointMutationSize = int(populationSize*0.12)# 12%
        self.allPointsMutationSize = int(populationSize*0.12) # 12%
        self.firstCrossOverSize = int(populationSize*0.20) # 20%
        self.secondCrossOverSize = int(populationSize*0.20) # 20%
        self.thirdCrossOverSize = int(populationSize*0.20)# 20%
        self.randomSize = int(populationSize*0.06) # 6%
                  
        self.population = []
        # pra acessar o fitness de cada indivíduo: population[i].fitness
                            
#        print('pb: ', self.previousBestsSize)
#        print('om: ', self.onePointMutationSize)
#        print('am: ', self.allPointsMutationSize)
#        print('fc: ', self.firstCrossOverSize)
#        print('sc: ', self.secondCrossOverSize)
#        print('tc: ', self.thirdCrossOverSize)
#        print('rn: ', self.randomSize)
        self.seed = seed
        random.seed(self.seed)
        
        # Initializing the population
        for x in range(self.populationSize):
            individuo = PMSPSolution.random_instance(restrictions)
            self.population.append(individuo)
        
        #ordena a população inicial (talvez não precise)
        self.population.sort(key=lambda x: x.fitness, reverse=False)
        

    def run(self, maxIterations):  
      random.seed(self.seed)
     
      top40 = int(self.populationSize * 0.4)
      top10 = int(self.populationSize * 0.1)
      
      op = Operators(self.restrictions)
      # Calculating each new generation
      for j in range(maxIterations):
        
        newPopulation=[]

        for i in range(self.previousBestsSize):
            newPopulation.append(self.population[i])
#            print('passando pra prox ', self.population[i].fitness)
        
        for i in range(self.onePointMutationSize):
            target = random.choice(self.population[0:top10]) #seleciona 1 entre os top 10 pra mutar
            newPopulation.append(op.onePointMutation(target))
        
        
        for i in range(self.allPointsMutationSize):
            target = random.choice(self.population[0:top10])
            newPopulation.append(op.allPointsMutation(target))
        
        for i in range(self.firstCrossOverSize):
            target1 = random.choice(self.population[0:top10])
            target2 = random.choice(self.population[0:top40])
            newPopulation.append(op.firstCrossOver(target1, target2))
        
        for i in range(int(self.secondCrossOverSize/2)):
            target1 = random.choice(self.population[0:top10])
            target2 = random.choice(self.population[0:top40])
            offspring = op.crossOver_Vallada(target1, target2)
            newPopulation.append(offspring[0])
            newPopulation.append(offspring[1])
                        
        for i in range(int(self.thirdCrossOverSize/2)):
            target1 = random.choice(self.population[0:top10])
            target2 = random.choice(self.population[0:top40])
            offspring = op.crossOver_Vallada_LocalSearch(target1, target2)
            newPopulation.append(offspring[0])
            newPopulation.append(offspring[1])            
            
        for i in range(self.randomSize):
            newInd = PMSPSolution.random_instance(self.restrictions)
            newPopulation.append(newInd)
    
        newPopulation.sort(key=lambda x: x.fitness, reverse=False)
        self.population = newPopulation
        print('gen ', j, ' best fitness: ', newPopulation[0].fitness)
#        for i in self.population:
#            print(i.fitness)

      return self.population[0]
