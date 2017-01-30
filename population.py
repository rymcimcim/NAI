from individual import Individual


class Population(object):

    def __init__(self, population_size, initialise):
        self.individuals = []
        if initialise:
            for i in range(0, population_size):
                new_individual = Individual()
                new_individual.generate_individual()
                # print(str(new_individual.get_fitness()))
                self.individuals.append(new_individual)

    def get_individual(self, index):
        return self.individuals[index]

    def set_individual(self, index, individual):
        self.individuals[index] = individual

    @property
    def fittest(self):
        fittest = self.individuals[0]
        for i in range(0, len(self.individuals)):
            if fittest.get_fitness() <= self.individuals[i].get_fitness():
                fittest = self.individuals[i]
        return fittest
