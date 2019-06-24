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

      self.populationSize = self.previousBestsSize + self.onePointMutationSize + \
                            self.allPointsMutationSize + self.meanCrossOversize + \
                            self.mediumPointCrossOverSize

      self.population = []
      # pra acessar o fitness de cada indivíduo: population[i].fitness
     

      # Initializing the population
      self.seed = seed
      
      for x in range(self.populationSize):
          individuo = PMSPSolution.random_instance(self.m, self.n, restrictions)
          self.population.append(individuo)

#    # Generates a random population where each weight of each solution is in the interval [a,b]
#    def randomizePopulation(self, a, b):
#      for i in range(self.populationSize):
#          self.population[i] =  PMSPSolution.random_instance(self.m, self.n, self.restrictions)
#   
    
    # Returns a list with the same size of self.population
    def createNewPopulation(self):
      newPopulation = []
      newFitness = []

      # Initializing the new population
      for i in range(self.populationSize):
        solution = []
        for j in range(self.numberOfWeights):
          solution.append(0.0)
        newPopulation.append(solution)
        newFitness.append(0.0)

      return newPopulation, newFitness

    # To determine which solutions have the best fitness
    # Implements selection sort
    def orderPopulationByFitness(self, population, fitness):
      minFitness = float("inf")
      minFitnessIndex = -1
      for i in range(len(population)):
        minFitness = fitness[i]
        minFitnessIndex = i

        # Finds the maximum value
        for j in range(i+1, len(population)):
          if self.fitness[j] < minFitness:
            minFitness = fitness[j]
            minFitnessIndex = j

        # Puts the minFitness and minFitnessIndex in their positions
        if minFitnessIndex != i:
          # Swaps the fitness
          aux = fitness[i]
          fitness[i] = fitness[minFitnessIndex]
          fitness[minFitnessIndex] = aux
          # Swaps the solutions
          auxSolution = population[i]
          population[i] = population[minFitnessIndex]
          population[minFitnessIndex] = auxSolution
      return population, fitness

    # Returns 0 if there was no increasing in the fitness value of any member of the population
    # Otherwise returns a positive number, which represent the number of positions which had it's fitness increased
    def improvementOfPopulation(self, newFitness):
      imp = 0
      for i in range(self.populationSize):
        if (newFitness[i] < self.fitness[i]):
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


    def run(self, evaluateFunction, maxIterations):
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
