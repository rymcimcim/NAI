from algorithm import Algorithm
from fitness_calc import FitnessCalc
from population import Population

fitness_calc = FitnessCalc()
fitness_calc.set_solution_str("1111000000000000000000000000000000000000000000000000000000001111")

population = Population(50, True)

generation_count = 0
# print(population.fittest.get_fitness())
while population.fittest.get_fitness() < fitness_calc.get_max_fitness():
    generation_count += 1
    print('Generation: ' + str(generation_count) + " Fittest: " + str(population.fittest.get_fitness()))

    population = Algorithm.evolve_population(population)

print("Solution found!")
print("Generation: " + str(generation_count))
print("Genes:")
print(population.fittest)
