# revised test file to combine population and mutations
# a population of Candidatus Pelagibacter will be created
# the population will have a carrying capacity of 300
# mutation rate = 0.003 mutations/genome * 1 genome/1.3 million bases = 
# 2.30769231e-9 mutations per base per generation

from organism import Organism
from environment import Environment
import random

fasta = open("./sequence.fasta", "r")
results = open("./results.txt", "w")

MUTATION_RATE = 0.0000000023
CARRYING_CAPACITY = 300

def parse_fasta(filename):
    sequence = ""
    for line in filename:
        if (not line.startswith(">")):
            sequence = sequence + line
    
    sequence.replace("\n", "")
    return sequence

candidatus = parse_fasta(fasta)
environment = Environment(MUTATION_RATE, CARRYING_CAPACITY)
organism = Organism(candidatus)
environment.population_list.append(organism)

def life_cycle():
    # runs through the full life of an immortal life form
    # theoretically this should be an infinite loop
    # 
    counter = 0
    for org in environment.population_list:
        if len(environment.population_list) >= CARRYING_CAPACITY:
            del environment.population_list[-1]
        org.transcribe()
        org.translate()
        environment.population_list.append(org.reproduce())
        rand = random.randint(0, (len(environment.population_list) - 1))
        environment.population_list[rand].DNA = environment.mutate(
                                                    environment.population_list[rand].DNA)
        
        results.write("Generation " + str(counter) + "\n")
        results.write(org.__repr__() + "\n")
        results.write(org.DNA + "\n")
        results.write("---------------------\n")
        counter += 1

life_cycle()