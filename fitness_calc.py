class FitnessCalc(object):
    solution_length = 64
    solution = []

    @staticmethod
    def set_solution(new_solution):
        FitnessCalc.solution = new_solution

    @staticmethod
    def set_solution_str(new_solution_string):
        FitnessCalc.solution = []
        for i in range(0, len(str(new_solution_string))):
            character = new_solution_string[i:i+1]
            if '0' in character or '1' in character:
                FitnessCalc.solution.append(int(character))
            else:
                FitnessCalc.solution.append(0)

    @staticmethod
    def get_fitness(individual):
        fitness = 0
        for i in range(0, individual.defaul_gene_length):
            if i in range(0, FitnessCalc.solution_length):
                if individual.get_gene(i) == FitnessCalc.solution[i]:
                    fitness += 1

        return fitness

    @staticmethod
    def get_max_fitness():
        return FitnessCalc.solution_length
