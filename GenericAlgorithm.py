from Individual import Individual
import random


class GenericAlgorithm ():
    def __init__(self, size_population):
        self.size_population = size_population
        self.population = []
        self.generation = 0
        self.best = 0

    def init(self, spaces, values, limit_spaces, mutation_more=0):
        for i in range(self.size_population):
            self.population.append(Individual(
                spaces, values, limit_spaces, 0, None, mutation_more))
            self.best = self.population[0]

    def order_population(self):
        self.population = sorted(
            self.population, key=lambda population: population.graduation, reverse=True)

    def bests_Individual(self, Individual):
        if Individual.graduation > self.best.graduation:
            self.best = Individual

    def some_avaliations(self):
        some = 0
        for Individual in self.population:
            some += Individual.graduation
        return some

    def select_fathers(self):
        fathers = []
        for _ in range(2):
            father = None
            sum_graduations = self.some_avaliations()
            rand_value = random.uniform(0, sum_graduations)
            some = 0
            for Individual in self.population:
                some += Individual.graduation
                if some > rand_value:
                    father = Individual
                    break
            fathers.append(father)
        return fathers
