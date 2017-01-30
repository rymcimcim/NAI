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
        new_population = Population(len(population.individuals), False)
        # print(Algorithm.__elitism)

        if Algorithm.__elitism:
            new_population.individuals.append(population.fittest)

        if Algorithm.__elitism:
            elitism_offset = 1
        else:
            elitism_offset = 0

        # print(new_population.individuals)
        for i in range(elitism_offset, len(new_population.individuals)):
            indiv1 = Algorithm.__tournament_selection(population)
            indiv2 = Algorithm.__tournament_selection(population)
            new_indiv = Algorithm.__crossover(indiv1, indiv2)
            new_population.individual(i, new_indiv)
        return new_population

    @staticmethod
    def __crossover(indiv1, indiv2):
        new_solution = Individual()

        for i in range(0, indiv1.defaul_gene_length):
            if random.random() <= Algorithm.__uniform_rate:
                new_solution.set_gene(i, indiv1.gene(i))
            else:
                new_solution.set_gene(i, indiv2.gene(i))

        return new_solution

    @staticmethod
    def __mutate(individual):
        for i in range(0, individual.defaul_gene_length):
            if random.random() <= Algorithm.__mutation_rate:
                individual.set_gene(i, random.randint(-128, 127))

    @staticmethod
    def __tournament_selection(population):
        tournament = Population(Algorithm.__tournament_size, False)

        for i in range(0, Algorithm.__tournament_size):
            random_id = random.random() * len(population.individuals)
            tournament.individual(i, population.individual(random_id))

        fittest = tournament.fittest
        return fittest
