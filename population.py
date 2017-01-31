from individual import Individual


class Population(object):

    def __init__(self, population_size, initialise):
        self.individuals = []
        if initialise:
            for i in range(0, population_size):
                new_individual = Individual()
                new_individual.generate_individual()
                self.save_individual(new_individual)
                self.individuals.append(new_individual)

    def get_individual(self, index):
        return self.individuals[index]

    def save_individual(self, individual):
        self.individuals.append(individual)

    def size(self):
        return len(self.individuals)

    def get_fittest(self):
        fittest = self.individuals[0]
        for i in range(0, self.size()):
            if fittest.get_fitness() <= self.get_individual(i).get_fitness():
                fittest = self.get_individual(i)
        return fittest
