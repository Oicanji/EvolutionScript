import random

from data import MUTATION_RATE


class Individuals():
    def __init__(self, products, values, limit, generation=0, gens=None):
        self.products = products
        self.values = values
        self.limit = limit
        self.spaces = 0
        self.generation = generation
        self.gens = gens if gens else self.create_gens(len(products))
        self.evaluetion = self.avaliation()

    def create_gens(self, size):
        list_gens = []
        for i in range(0, size):
            result = random.choice([0, 1])
            list_gens.append(result)
        return list_gens

    def crossover(self, other):
        cut = round(random.random() * len(self.gens))

        child1 = other.gens[0:cut] + self.gens[cut::]
        child2 = self.gens[0:cut] + other.gens[cut::]

        return  (Individuals(self.products, self.values, self.limit, self.generation + 1, self.mutation(MUTATION_RATE, child1)),
                  Individuals(self.products, self.values, self.limit, self.generation + 1, self.mutation(MUTATION_RATE, child2)))

        # childs[0].gens = child1
        # childs[1].gens = child2

        # return childs

    def mutation(self, tax, gens):
        for i in range(len(gens)):
            if random.randint(0, 100) < tax:
                if gens[i] == 1:
                    gens[i] = 0
                else:
                    gens[i] = 1
        return gens

    def __str__(self) -> str:
        return self.gens.__str__()

    def avaliation(self):
        grade = 0
        self.spaces = 0
        print(self.gens)
        for index, gen in enumerate(self.gens):
            print(gen)
            if gen == 1:
                grade += self.values[index]
                self.spaces += self.products[index]
        print("self.spaces", self.spaces, "self.limit",  self.limit)
        if self.spaces > self.limit:
            return 1
        return grade
