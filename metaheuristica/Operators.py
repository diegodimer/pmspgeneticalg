import random
import math
import PMSPRestrictions
import PMSPSolution

class Operators:
    def __init__(self, 
                 restrictions: PMSPRestrictions):
        self.restrictions = restrictions
        

    # Adds a value between (-1.0, 1.0) / self.scale to one weight
    def onePointMutation(self, 
                         solution: PMSPSolution, 
                         mutationScale):
      
#        newSolution = []
#      for i in range(self.numberOfWeights):
#        newSolution.append(solution[i])
#      mutationSite = random.randrange(0, len(solution))
#      newSolution[mutationSite] += random.uniform(-1.0, 1.0) / mutationScale
#      return newSolution
        raise NotImplemented

    # Adds a value between (-1.0, 1.0) / self.scale to each weight
    def allPointsMutation(self, 
                          solution: PMSPSolution, 
                          mutationScale):
#      newSolution = []
#      for i in range(self.numberOfWeights):
#        newSolution.append(solution[i] + (random.uniform(-1.0, 1.0) / mutationScale))
#      return newSolution
        raise NotImplemented

    # Returns the mean of the two solutions
    def meanCrossOver(self, 
                      solution1: PMSPSolution, 
                      solution2: PMSPSolution):
#      newSolution = []
#      for i in range(len(solution1)):
#        newValue = (solution1[i] + solution2[i]) / 2.0
#        newSolution.append(newValue)
#      return newSolution
        raise NotImplemented

    # newSolution takes the first half of the weights from solution1 and the other half from solution2
    def mediumPointCrossOver(self, 
                             solution1: PMSPRestrictions, 
                             solution2: PMSPRestrictions):
#      newSolution = []
#      for i in range(len(solution1)):
#        if i < len(solution1) / 2:
#          newSolution.append(solution1[i])
#        else:
#          newSolution.append(solution2[i])
#      return newSolution
        raise NotImplemented