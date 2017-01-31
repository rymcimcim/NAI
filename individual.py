import random

from fitness_calc import FitnessCalc


class Individual(object):
    defaul_gene_length = 64

    def __init__(self):
        self.__genes = []

        self.__fitness = 0

    def __str__(self):
        return str(self.__genes)

    def generate_individual(self):
        for i in range(0, self.defaul_gene_length):
            gene = round(random.random())
            self.__genes.append(gene)

    def size(self):
        return len(self.__genes)

    def get_fitness(self):
        if self.__fitness == 0:
            self.__fitness = FitnessCalc.get_fitness(self)
        return self.__fitness

    def get_defaul_gene_length(self):
        return self.defaul_gene_length

    def get_gene(self, index):
        return self.__genes[index]

    def set_gene(self, value):
        self.__genes.append(value)
        self.__fitness = 0

    def set_gene_index(self, index, value):
        self.__genes[index] = value
        self.__fitness = 0
