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
                            
        print('pb: ', self.previousBestsSize)
        print('om: ', self.onePointMutationSize)
        print('am: ', self.allPointsMutationSize)
        print('fc: ', self.firstCrossOverSize)
        print('sc: ', self.secondCrossOverSize)
        print('tc: ', self.thirdCrossOverSize)
        print('rn: ', self.randomSize)
        self.seed = seed
        random.seed(self.seed)
        
        # Initializing the population
        for x in range(self.populationSize):
            individuo = PMSPSolution.random_instance(restrictions)
            self.population.append(individuo)
        
        #ordena a população inicial (talvez não precise)
        self.population.sort(key=lambda x: x.fitness, reverse=False)
        

    # Ordena a população recebida como parâmetro de acordo com o fitness dela
    @staticmethod
    def orderPopulationByFitness(population: list):
        population = sorted(population, key=lambda x: x.fitness, reverse=False)
        return population

    # Returns 0 if there was no increasing in the fitness value of any member of the population
    # Otherwise returns a positive number, which represent the number of positions which had it's fitness increased
    def improvementOfPopulation(self,
                                newPopulation: list):
      imp = 0
      for i in range(self.populationSize):
        if (newPopulation[i].fitness < self.population[i].fitness):
          imp += 1
      return imp


    def run(self, maxIterations):  
      random.seed(self.seed)
      
      newPopulation=[];
      
      top40 = int(self.populationSize * 0.4)
     
      top10 = int(self.populationSize * 0.1)
      
      op = Operators(self.restrictions)
      # Calculating each new generation
      for j in range(maxIterations):
        

        for i in range(self.previousBestsSize):
            newPopulation.append(self.population[i])
        
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
    
        self.population = GeneticAlgorithm.orderPopulationByFitness(newPopulation)
        print('gen ', j, ' best fitness: ', self.population[0].fitness)
 
      return self.population[0]
