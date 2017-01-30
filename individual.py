import random

from fitness_calc import FitnessCalc


class Individual(object):
    def __init__(self):
        self.__defaul_gene_length = 64
        self.__byte_list = []

        self.__fitness_value = 0

    def generate_individual(self):
        for i in range(0, self.__defaul_gene_length):
            gene = round(random.random())
            # print(gene)
            self.__byte_list.append(gene)

    def get_fitness(self):
        if self.__fitness_value == 0:
            fitness_calc = FitnessCalc()
            self.__fitness_value = fitness_calc.get_fitness(self)
        return self.__fitness_value

    @property
    def defaul_gene_length(self):
        return self.__defaul_gene_length

    @defaul_gene_length.setter
    def defaul_gene_length(self, value):
        self.__defaul_gene_length = value

    def get_gene(self, index):
        return self.__byte_list[index]

    def set_gene(self, index, value):
        self.__byte_list[index] = value
        self.__fitness_value = 0
