import random
import math
from PMSPRestrictions import PMSPRestrictions
from PMSPSolution import PMSPSolution
import Operators


class GeneticAlgorithm:
    def __init__(self, 
                 restrictions: PMSPRestrictions, 
                 populationSize: int,
                 seed = None):
        self.m = restrictions.m
        self.n = restrictions.n
        self.restrictions = restrictions
        self.operators = Operators.Operators(restrictions)

        self.populationSize =   populationSize
        
        # Number of solutions generated per operator
        self.previousBestsSize = 5
        self.onePointMutationSize = 5
        self.allPointsMutationSize = 5
        self.firstCrossOverSize = 5
        self.secondCrossOverSize = 5
        self.thirdCrossOverSize = 5
                  
        self.population = []
        # pra acessar o fitness de cada indivíduo: population[i].fitness
                                
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
      # Calculating each new generation
      for j in range(maxIterations):
        print("Generation " + str(j))
        offset = 0
        for i in range(self.previousBestsSize):
          # Copies from previous population
          newPopulation.append(self.population[i])

        offset = self.previousBestsSize
        
        for i in range(self.onePointMutationSize):
          # onePointMutation()
          solution = random.choice(self.population)
          newPopulation.append(self.operators.onePointMutation(solution, 1))

        offset += self.onePointMutationSize
        for i in range(self.allPointsMutationSize):
          # allPointsMutation()
          solution = random.choice(self.population)
          newPopulation.append(self.operators.allPointsMutation(solution, 1))

        offset += self.allPointsMutationSize
        limit = self.populationSize/4 # seleciona os 1/4 melhores da população
        
        for i in range(self.meanCrossOversize):
          # meanCrossOver()
          solution1 = self.population[random.randint(0,limit)]
          solution2 = random.choice(self.population)
          newPopulation.append(self.operators.meanCrossOver(solution1, solution2))

        offset += self.meanCrossOversize
        for i in range(self.mediumPointCrossOverSize):
          # mediumPointCrossOver()
          solution1 = self.population[random.randint(0, limit)]
          solution2 = random.choice(self.population)
          newPopulation.append(self.operators.firstCrossOver(solution1, solution2))

      
        self.population = GeneticAlgorithm.orderPopulationByFitness(newPopulation)
        print('gen ', j, ' best fitness: ', self.population[0].fitness)
 
      return self.population[0]
