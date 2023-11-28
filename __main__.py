from algorithm import AlgorithmGeneric
from data import GENERATIONS, POPULATION_SIZE, SPACE_LIMIT, list_product
import tkinter as tk
from tkinter import simpledialog, messagebox
from matplotlib import pyplot as plt

print("Welcome to EvolutionScript!")


def main():
    ag = AlgorithmGeneric(POPULATION_SIZE)
    ag.init_population(
        [list_productz.space for list_productz in list_product],
        [list_productz.value for list_productz in list_product], SPACE_LIMIT)
    population_initial = ag.population
    bests = []

    for _ in range(GENERATIONS):
        ag.order_population()

        best_of_generation = ag.population[0]
        print("Geração:", ag.population[0])
        bests.append(best_of_generation)

        ag.best_individual(best_of_generation)

        sum_evaluations = ag.sum()

        new_population = []

        print("population_size:", ag.population_size)
        for _ in range(0, ag.population_size, 2):
            fathers = ag.select_fathers()
            print("Parents:", fathers)
            children = fathers[0].crossover(fathers[1])

            for child in children:
                new_population.append(child)

        ag.population = new_population
        ag.generation += 1

    bests.append(best_of_generation)

    print("Melhor solução:")
    print("Cromossomo:", ag.best.gen)
    print("Espaços usados:", ag.best.spaces)
    print("Valores obtidos:", ag.best.values)
    print("Preço total da mochila", ag.best.evaluetion)

    def create_chart(res):
        generations = list(range(1, len(res) + 1))
        totals = [ind.evaluetion for ind in res]

        plt.plot(generations, totals, marker='o', linestyle='-')
        plt.title('Evolução do Preço Total na Mochila por Geração')
        plt.xlabel('Geração')
        plt.ylabel('Preço Total na Mochila')
        plt.grid(True)
        plt.show()

    create_chart(bests)


main()
