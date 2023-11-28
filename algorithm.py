import random
from individuals import Individuals


class AlgorithmGeneric:
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = []
        self.generation = 0
        self.best = 0

    def init_population(self, spaces, values, limit_space):
        for i in range(self.population_size):
            self.population.append(Individuals(spaces, values, limit_space))
            self.best = self.population[0]

    def order_population(self):
        self.population = sorted(
            self.population, key=lambda population: population.evaluetion, reverse=True)

    def best_individual(self, individual):
        if individual.evaluetion > self.best.evaluetion:
            self.best = individual

    def sum(self):
        totals = 0
        for ind in self.population:
            totals += ind.evaluetion
        return totals

    def select_fathers(self):
        fathers = []
        for _ in range(2):
            father = None
            sum_eval = self.sum()
            rand_val = random.uniform(0, sum_eval)
            sum_int = 0
            for ind in self.population:
                sum_int += ind.evaluetion
                if sum_int >= rand_val:
                    father = ind
                    break
            fathers.append(father)
        return fathers
