from tkinter import *
import tkinter
from tkinter import messagebox
from GenericAlgorithm import GenericAlgorithm
from data import GENERATION, LIMIT, LIST, POPULATION
from Product import Product
from matplotlib import pyplot as plt


import random


def plot(list_best_mutations, title):
    fig, axs = plt.subplots(len(list_best_mutations), 1,
                            figsize=(10, 6 * len(list_best_mutations)))

    fig.suptitle(title, fontsize=16)
    for i, res in enumerate(list_best_mutations):
        geracoes = list(range(1, len(res) + 1))
        values_totais = [Individual.graduation for Individual in res]

        # Gerando uma cor aleatória
        cor = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        axs[i].plot(geracoes, values_totais, linestyle='-', color=cor)
        axs[i].set_title(
            f'Evolução do Preço Total na Mochila (Mutação {i + 1})', fontsize=5)
        axs[i].set_xlabel('Geração', fontsize=5)
        axs[i].set_ylabel('Preço Total na Mochila', fontsize=5)

        # Removendo os marcadores (bolinhas)
        axs[i].plot(geracoes, values_totais,
                    linestyle='-', color=cor, marker='')

        # Definindo limites para os eixos y
        min_value = min(values_totais)
        max_value = max(values_totais)
        axs[i].set_ylim([min_value - 0.1 * abs(min_value),
                        max_value + 0.1 * abs(max_value)])

        # Ajustando a legibilidade dos valores nos eixos y
        axs[i].tick_params(axis='y', labelsize=5)
        axs[i].tick_params(axis='x', labelsize=5)

        axs[i].grid(True)

    plt.tight_layout()
    plt.show()


def process(mutation_more, generation=0):
    spaces = [item['inches'] for item in LIST]
    values = [item['value'] for item in LIST]

    ag = GenericAlgorithm(POPULATION)
    ag.init(spaces, values, LIMIT, mutation_more)
    bests = []

    for _ in range(GENERATION+(generation*100)):
        ag.order_population()

        best_of_this_generation = ag.population[0]
        bests.append(best_of_this_generation)

        ag.bests_Individual(best_of_this_generation)

        nova_population = []

        for _ in range(0, ag.size_population, 2):
            fathers = ag.select_fathers()
            filhos = fathers[0].crossover(fathers[1])

            for filho in filhos:
                nova_population.append(filho)

        ag.population = nova_population
        ag.generation += 1

    return bests


def main(num_mutacoes, num_geracoes):
    # criando Products

    list_best_mutations = []
    if (num_mutacoes > 0):
        for i in range(1, num_mutacoes + 1):
            list_best_mutations.append(process(i*5))

    plot(list_best_mutations, "Variação na mutação")

    list_best_generations = []
    if (num_geracoes > 0):
        for i in range(1, num_geracoes + 1):
            list_best_generations.append(process(0, i))

    plot(list_best_generations, "Variação na geração")


root = Tk()


def obter_valores(mutacoes_entry, geracoes_entry):
    num_mutacoes = int(mutacoes_entry.get() or 0)
    num_geracoes = int(geracoes_entry.get() or 0)

    print("Número de mutações: ", num_mutacoes,
          "Número de gerações: ", num_geracoes)
    main(num_mutacoes, num_geracoes)
    root.destroy()


def criar_interface():
    root.title("Configurações do Algoritmo Genético")

    Label(root, text="Número Maximo de Mutação (soma +5):").grid(row=0, column=0)
    mutacoes_entry = Entry(root)
    mutacoes_entry.grid(row=0, column=1)

    Label(root, text="Número de Gerações (soma +100 a cada):").grid(row=1, column=0)
    geracoes_entry = Entry(root)
    geracoes_entry.grid(row=1, column=1)

    Button(root, text="Iniciar", command=lambda: obter_valores(
        mutacoes_entry, geracoes_entry)).grid(row=2, column=1)

    root.mainloop()
