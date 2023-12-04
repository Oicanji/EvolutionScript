import random
from data import MUTATION


class Individual ():
    def __init__(self, spaces, values, limit_spaces, generation=0, chromosomes=None, mutation_more=0):
        self.spaces = spaces
        self.values = values
        self.limit_spaces = limit_spaces
        self.used = 0
        self.generation = generation
        self.chromosomes = chromosomes if chromosomes else self.create_chromosomes(
            len(spaces))
        self.graduation = self.eval()
        self.mutation_more = mutation_more

    def create_chromosomes(self, tm):
        lista_chromosomes = []
        for i in range(0, tm):
            result = random.choice([0, 1])
            lista_chromosomes.append(result)
        return lista_chromosomes

    def crossover(self, others):
        cut = round(random.random() * len(self.chromosomes))
        first_child = others.chromosomes[0:cut] + \
            self.chromosomes[cut::]
        other_child = self.chromosomes[0:cut] + \
            others.chromosomes[cut::]
        # filhos = [Individual( self.spaces, self.values ,self.limit_spaces ,self.generation + 1),
        #          Individual ( self.spaces ,self.values ,self.limit_spaces ,self.generation + 1) ]
        # filhos[0].chromosomes = first_child
        # filhos[1].chromosomes = other_child

        return (
            Individual(self.spaces, self.values, self.limit_spaces,
                       self.generation + 1, self.mutation(MUTATION+self.mutation_more, first_child), self.mutation_more),
            Individual(self.spaces, self.values, self.limit_spaces,
                       self.generation + 1, self.mutation(MUTATION+self.mutation_more, other_child), self.mutation_more)
        )

    def mutation(self, mutation, chromosomes):
        for i in range(len(chromosomes)):
            if random.randint(0, 100) < mutation:
                if chromosomes[i] == 1:
                    chromosomes[i] = 0
                else:
                    chromosomes[i] = 1
        return chromosomes
    # converte objeto para uma str

    def __str__(self) -> str:
        return self.chromosomes.__str__()

    def eval(self):
        grade = 0
        self.used = 0
        for index, item in enumerate(self.chromosomes):
            if item == 1:
                grade += self.values[index]
                self.used += self.spaces[index]
        if self.used > self.limit_spaces:
            return 1
        return grade
