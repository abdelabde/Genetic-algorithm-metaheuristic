'''1-Core Coding'''
'''importing packges'''
import matplotlib as plt
import random
import math
import statistics as st
'''Selection stage'''
def generate_population(size, lower_x_boundary=-100,upper_x_boundary=100):
    population = []
    while len(population)<size:
        individual =random.uniform(lower_x_boundary, upper_x_boundary)
        if individual!=0:
            population.append(individual)
    return population
'''Fitness function'''
def apply_function(individual):
    x = individual
    return (x/10)*(17-200/math.exp(-24/x))+21

'''selection by roulette'''
def choice_by_roulette(sorted_population, fitness_sum):
    offset = 0
    normalized_fitness_sum = fitness_sum
    lowest_fitness = apply_function(sorted_population[0])
    if lowest_fitness < 0:
        offset = -lowest_fitness
        normalized_fitness_sum += offset * len(sorted_population)

    draw = random.uniform(0, 1)

    accumulated = 0
    for individual in sorted_population:
        fitness = apply_function(individual) + offset
        probability = fitness / normalized_fitness_sum
        accumulated += probability

        if draw <= accumulated:
            return individual
def sort_population_by_fitness(population):
    return sorted(population, key=apply_function)


def crossover(individual):

    return(individual*0.7)

def mutate(individual):
    next_x = individual+ random.uniform(-10, 10)
    return next_x
def make_next_generation(previous_population):
    next_generation = []
    sorted_by_fitness_population = sort_population_by_fitness(previous_population)
    population_size = len(previous_population)
    fitness_sum = sum(apply_function(individual) for individual in population)
    for i in range(population_size):
        first_choice = choice_by_roulette(sorted_by_fitness_population, fitness_sum)
        individual = crossover(first_choice)
        individual = mutate(individual)
        next_generation.append(individual)

    return next_generation
'''1-Result analysis'''
generations =100
L_best_individual=[]
L_fitness_best_individual=[]
L_Average_fitness=[]
for j in range(5):
    population = generate_population(size=100, lower_x_boundary=-100,upper_x_boundary=100)
    i = 1
    L=[]
    while True:
        for individual in population:
            print(individual, apply_function(individual))
            L.append(apply_function(individual))
    
        if i == generations:
            break
    
        i += 1
    
        population = make_next_generation(population)
    
    best_individual = sort_population_by_fitness(population)[-1]
    L_best_individual.append(best_individual )
    L_fitness_best_individual.append(apply_function(best_individual))
    L_Average_fitness.append(st.mean(L))
    
plt.plot([i for i in range(5)],L_fitness_best_individual)
plt.show()
plt.plot([i for i in range(5)],L_Average_fitness)
plt.show()

'''According to the plots the GA will have a convergence to a best element that gives optimal solution'''


