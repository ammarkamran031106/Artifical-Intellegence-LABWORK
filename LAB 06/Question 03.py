#Task 3 – Genetic Algorithm
#Use a Genetic Algorithm to maximize the function
#f(x) = x2 + 2x
#Range: 0 ≤ x ≤ 31
#Instructions:
#• Use binary representation for chromosomes.
#• Generate a random initial population.
#• Calculate fitness using the function f(x).
#• Apply selection, crossover, and mutation.
#• Run the algorithm for 15 generations.
#Output should show:
#• Best chromosome
#• Best value of x
#• Best fitness value.


import random

# fitness function
def fitness(x):
    return x*x + 2*x

# convert binary to decimal
def decode(ch):
    return int(ch,2)

# random chromosome (5 bits)
def random_chrom():
    ch = ""
    for i in range(5):
        ch += str(random.randint(0,1))
    return ch

# crossover
def crossover(p1,p2):
    point = random.randint(1,4)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1,c2

# mutation
def mutation(ch):
    i = random.randint(0,4)
    ch = list(ch)
    ch[i] = '1' if ch[i]=='0' else '0'
    return "".join(ch)

# Genetic Algorithm
population = []
for i in range(6):
    population.append(random_chrom())

for gen in range(15):

    # sort population by fitness
    population.sort(key=lambda x: fitness(decode(x)), reverse=True)

    p1 = population[0]
    p2 = population[1]

    new_pop = []

    for i in range(3):
        c1,c2 = crossover(p1,p2)

        if random.random() < 0.1:
            c1 = mutation(c1)
        if random.random() < 0.1:
            c2 = mutation(c2)

        new_pop.append(c1)
        new_pop.append(c2)

    population = new_pop


# best solution
population.sort(key=lambda x: fitness(decode(x)), reverse=True)

best = population[0]
x = decode(best)

print("Best Chromosome:",best)
print("Best value of x:",x)
print("Best fitness value:",fitness(x))
