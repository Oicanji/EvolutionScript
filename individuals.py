import random


class Individuals():
    def __init__(self, spaces, products, limit, generation=0, gens=None):
        self.generation = generation
        self.products = products
        self.limit = limit
        self.evaluetion = 0
        self.spaces = spaces
        self.generation = 0
        self.gen = gens if gens else self.create_gens(len(spaces))

    def create_gens(self, size):
        list_gens = []
        for i in range(0, size):
            result = random.choice([0, 1])
            list_gens.append(result)
        return list_gens

    def vals(self):
        for i in range(len(self.gen)):
            if self.gen[i] == 1:
                self.spaces += self.products[i].space
                self.evaluetion += self.products[i].value

        if self.spaces > self.limit:
            self.evaluetion = 1
        return self.spaces, self.evaluetion

    def crossover(self, other):
        cut = random.randint(0, len(self.gen) - 1)

        child1 = other.gen[0:cut] + self.gen[cut::]
        child2 = self.gen[0:cut] + other.gen[cut::]

        childs = [Individuals(self.spaces, self.products, self.limit, self.generation + 1),
                  Individuals(self.spaces, self.products, self.limit, self.generation + 1)]

        childs[0].gen = child1
        childs[1].gen = child2

        return childs

    def mutation(self, tax, gen):
        for i in range(len(gen)):
            if random.random() < tax:
                if gen[i] == 1:
                    gen[i] = 0
                else:
                    gen[i] = 1
        return gen

    def __str__(self) -> str:
        return self.gen.__str__()

    def avaliation(self):
        grade = 0
        self.spaces = 0
        for index, item in enumerate(self.cromossomo):
            if item == 1:
                grade += self.products[index].value
                self.spaces += self.products[index].space
        if self.spaces > self.limite_espacos:
            return 1
        return grade
