import random
from math import ceil

def create_individual(orig, size):
    individual = list(range(0,size))
    random.shuffle(individual)
    individual.remove(orig)
    individual.insert(0, orig)
    return individual


def calculate_fitness(individual, dist_matrix, size):
    individual_route = 0
    for i in range(size-1):
        individual_route += dist_matrix[individual[i]][individual[i+1]]

    individual_route += dist_matrix[individual[-1]][individual[0]]
    return individual_route

def select_parents(population, fitness, number_of_parents):
    parents = []
    for i in range(number_of_parents):
        min_fitness = min(fitness)
        min_fitness_index = fitness.index(min_fitness)
        parents.append(population[min_fitness_index])
        fitness.pop(min_fitness_index)
        population.pop(min_fitness_index)
    
    return parents

def crossover(parents, number_of_offspring, length):
    offspring = []

    for i in range(number_of_offspring):
        a=random.randint(0,len(parents)-1)
        b=random.randint(0,len(parents)-1)
        child = parents[a][0:ceil(length/2)]
        for j in range (length):
            if parents[b][j] not in child:
                child.append(parents[b][j])
        offspring.append(child)
    
    return offspring


def mutation(individual, mutation_rate):
    occurence = random.randint(0,100)
    length = len(individual)
    if occurence <= mutation_rate:
        gene_one = random.randint(1,length-1)
        gene_two = random.randint(1,length-1)
        pom = individual[gene_one]
        individual[gene_one] = individual[gene_two]
        individual[gene_two] = pom

    return individual