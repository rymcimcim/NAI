import random

from individual import Individual
from population import Population


class Algorithm(object):
    __uniform_rate = float(0.5)
    __mutation_rate = float(0.015)
    __tournament_size = 5
    __elitism = True

    @staticmethod
    def evolve_population(population):
        new_population = Population(population.size(), False)

        if Algorithm.__elitism:
            new_population.save_individual(population.get_fittest())

        if Algorithm.__elitism:
            elitism_offset = 1
        else:
            elitism_offset = 0

        # print(new_population.individuals)
        for i in range(elitism_offset, population.size()):
            indiv1 = Algorithm.__tournament_selection(population)
            indiv2 = Algorithm.__tournament_selection(population)
            new_indiv = Algorithm.__crossover(indiv1, indiv2)
            new_population.save_individual(new_indiv)

        for i in range(elitism_offset, new_population.size()):
            Algorithm.__mutate(new_population.get_individual(i))

        return new_population

    @staticmethod
    def __crossover(indiv1, indiv2):
        new_solution = Individual()

        for i in range(0, indiv1.defaul_gene_length):
            if random.random() <= Algorithm.__uniform_rate:
                new_solution.set_gene(indiv1.get_gene(i))
            else:
                new_solution.set_gene(indiv2.get_gene(i))

        return new_solution

    @staticmethod
    def __mutate(individual):
        for i in range(0, individual.defaul_gene_length):
            if random.random() <= Algorithm.__mutation_rate:
                individual.set_gene_index(i, round(random.random()))

    @staticmethod
    def __tournament_selection(population):
        tournament = Population(Algorithm.__tournament_size, False)

        for i in range(0, Algorithm.__tournament_size):
            random_id = int(random.random() * len(population.individuals))
            tournament.save_individual(population.get_individual(random_id))

        fittest = tournament.get_fittest()
        return fittest
