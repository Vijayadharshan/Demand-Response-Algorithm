import math
import random


from optimization.fitness import fitnessfunc


class gwo:
    def __init__(self, population_size, iterations):
        self.population_size = population_size
        self.iterations = iterations

    def calculate_power_reduction(self, appliances, solution):
        reduction = 0
        for i in range(len(appliances)):
            if solution[i] == 0 and appliances[i].state:
                reduction += appliances[i].rated_power
        return reduction

    def calculate_comfort_penalty(self, appliances, solution):
        penalty = 0
        for i in range(len(appliances)):
            if solution[i] == 0 and appliances[i].state:
                penalty += appliances[i].comfort / 10
        return penalty

    def calculate_fitness(self, appliances, solution, reduction_req):
        reduction = self.calculate_power_reduction(appliances, solution)
        switches = self.count_switches(appliances, solution)
        comfort_penalty = self.calculate_comfort_penalty(appliances, solution)
        fitness_function = fitnessfunc(reduction_req)
        fitness = fitness_function.calculate(reduction, switches, comfort_penalty)
        return fitness


    def initialize_population(self, no_of_appliances):
        population = []
        for _ in range(self.population_size ):
            solution = []
            for _ in range(no_of_appliances):
                solution.append(random.randint(0, 1))
            population.append(solution)
        return population

    def count_switches(self, appliances, solution):
        switches = 0
        for i in range(len(appliances)):
            if appliances[i].state and solution[i] == 0:
                switches += 1
        return switches

    def optimize(self, appliances, reduction_req):

        no_of_appliances = len(appliances)
        population = self.initialize_population(no_of_appliances)
        alpha = None
        beta = None
        delta = None

        alpha_fitness = float('inf')
        beta_fitness = float('inf')
        delta_fitness = float('inf')

        for iteration in range(self.iterations):
            for solution in population:
                fitness = self.calculate_fitness(appliances, solution, reduction_req)
                if fitness < alpha_fitness:
                    delta = beta
                    delta_fitness = beta_fitness
                    beta = alpha
                    beta_fitness = alpha_fitness
                    alpha = solution.copy()
                    alpha_fitness = fitness
                elif fitness < beta_fitness:
                    delta = beta
                    delta_fitness = beta_fitness
                    beta = solution.copy()
                    beta_fitness = fitness
                elif fitness < delta_fitness:
                    delta = solution.copy()
                    delta_fitness = fitness

            a = 2 -  (2*iteration / self.iterations)

            new_population = []
            for soliton in population:
                new_soluiton = []
                for j in range(no_of_appliances):
                    r1 = random.random()
                    r2 = random.random()
                    A1 = 2*a*r1-a
                    C1 = 2*r2
                    D_alpha = abs(C1*alpha[j]-soliton[j])
                    X1 = alpha[j]-A1*D_alpha

                    r1 = random.random()
                    r2 = random.random()
                    A2 = 2 * a * r1 - a
                    C2 = 2 * r2
                    D_beta = abs(C2 * beta[j] - soliton[j])
                    X2 = beta[j] - A2 * D_beta

                    r1 = random.random()
                    r2 = random.random()
                    A3 = 2 * a * r1 - a
                    C3 = 2 * r2
                    D_delta = abs(C3 * delta[j] - soliton[j])
                    X3 = delta[j] - A3 * D_delta

                    X = (X1 + X2 + X3) / 3
                    probability = 1/(1+math.exp(-X))
                    if random.random()<probability:
                        new_soluiton.append(1)
                    else:
                        new_soluiton.append(0)
                new_population.append(new_soluiton)
            population = new_population
        return alpha






