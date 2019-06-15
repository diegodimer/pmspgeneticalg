import math

import GeneticAlgorithm


def evaluate(param):
    squaredError = 0.0
    for i in range(10):
        a = 3.14
        b = -1.15
        c = 2.36
        d = -11.55

        expected = a * math.pow(i, 3) + b * math.pow(i, 2) + c * float(i) + d
        value = param[0] * math.pow(i, 3) + param[1] * math.pow(i, 2) + param[2] * float(i) + param[3]

        squaredError += math.pow(expected - value, 2)

    return math.sqrt(squaredError)

if __name__ == '__main__':
    ga = GeneticAlgorithm.GeneticAlgorithm(4)
    ga.run(evaluate, 200)

