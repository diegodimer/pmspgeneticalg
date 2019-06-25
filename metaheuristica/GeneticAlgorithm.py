import random
import math
import PMSPRestrictions
import PMSPSolution
import Operators


class GeneticAlgorithm:
    def __init__(self, 
                 restrictions: PMSPRestrictions, 
                 seed = None):
        self.m = restrictions.m
        self.n = restrictions.n
        self.restrictions = restrictions
        self.operators = Operators.Operators(restrictions)

        # Number of solutions generated per operator
        self.previousBestsSize = 5
        self.onePointMutationSize = 5
        self.allPointsMutationSize = 5
        self.meanCrossOversize = 5
        self.mediumPointCrossOverSize = 5
          
        self.populationSize =   self.previousBestsSize + self.onePointMutationSize + \
                                self.allPointsMutationSize + self.meanCrossOversize + \
                                self.mediumPointCrossOverSize
                                
        self.population = []
        # pra acessar o fitness de cada indivíduo: population[i].fitness
                                
        self.seed = seed
        # Initializing the population
        for x in range(self.populationSize):
            individuo = PMSPSolution.random_instance(self.m, self.n, restrictions)
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


    def createMatingPool(self):
      matingPool = []
      for i in range(self.populationSize):
        # 5 times so each solution has at least 5 appearances
        appearancesI = round(5 * self.fitness[self.populationSize-1] / self.fitness[i])
        for j in range(appearancesI):
          matingPool.append(self.population[i])
      return matingPool


    def run(self, maxIterations):
      random.seed(self.seed)
      for i in range(self.populationSize):
        self.fitness[i] = evaluateFunction(self.population[i])

      self.population, self.fitness = self.orderPopulationByFitness(self.population, self.fitness)
      newPopulation, newFitness = self.createNewPopulation()

      # Calculating each new generation
      for i in range(maxIterations):
        print("Generation " + str(i))
        matingPool = self.createMatingPool()

        offset = 0
        # Calculating the new population
        for i in range(self.previousBestsSize):
          # Copies from previous population
          newPopulation[i + offset] = self.population[i]

        offset += self.previousBestsSize
        for i in range(self.onePointMutationSize):
          # onePointMutation()
          solution = random.choice(matingPool)
          newPopulation[i + offset] = self.operators.onePointMutation(solution, self.mutationScale)

        offset += self.onePointMutationSize
        for i in range(self.allPointsMutationSize):
          # allPointsMutation()
          solution = random.choice(matingPool)
          newPopulation[i + offset] = self.operators.allPointsMutation(solution, self.mutationScale)

        offset += self.allPointsMutationSize
        for i in range(self.meanCrossOversize):
          # meanCrossOver()
          solution1 = random.choice(matingPool)
          solution2 = random.choice(matingPool)
          newPopulation[i + offset] = self.operators.meanCrossOver(solution1, solution2)

        offset += self.meanCrossOversize
        for i in range(self.mediumPointCrossOverSize):
          # mediumPointCrossOver()
          solution1 = random.choice(matingPool)
          solution2 = random.choice(matingPool)
          newPopulation[i + offset] = self.operators.mediumPointCrossOver(solution1, solution2)

        for i in range(self.populationSize):
            #print("Evaluating " + str(newPopulation[i]))
            newFitness[i] = evaluateFunction(newPopulation[i])

        newPopulation, newFitness = self.orderPopulationByFitness(newPopulation, newFitness)

        print(newFitness[0])

        self.population = newPopulation
        self.fitness = newFitness

        self.mutationScale *= 2
        if self.mutationScale > self.maxMutationScale:
          self.mutationScale = self.maxMutationScale

      print(self.population[0])
      return self.population[0]
