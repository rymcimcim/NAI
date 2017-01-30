class FitnessCalc(object):
    solution_length = 64
    solution_list = []

    def get_solution(self, index):
        return self.solution_list[index]

    def set_solution(self, new_solution):
        self.solution_list = new_solution

    def set_solution_str(self, new_solution_string):
        for i in range(0, len(str(new_solution_string))):
            character = new_solution_string[i:i+1]
            if '0' in character or '1' in character:
                self.solution_list.append(int(character))
            else:
                self.solution_list.append(0)

    def get_fitness(self, individual):
        fitness = 0
        for i in range(0, individual.defaul_gene_length):
            if i in range(0, len(self.solution_list)):
                if individual.get_gene(i) == self.solution_list[i]:
                    # print(individual.get_gene(i), self.solution_list[i])
                    fitness += 1

        return fitness

    def get_max_fitness(self):
        return self.solution_length
