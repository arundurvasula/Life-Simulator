from organism import Organism
from environment import Environment
from sys import argv
import time

# what a mess.

filename = argv[1]
fasta = open(filename,"r")


def parse_fasta(filename):
    sequence = ""
    for line in filename:
        if (not line.startswith(">")):
            sequence = sequence + line
    
    sequence.replace("\n", "")
    return sequence

sequence = parse_fasta(fasta)
environment = Environment(0.000000001, 10)
organism = Organism(sequence) 
environment.population_list.append(organism)

start = time.clock()
for organism in environment.population_list:
    
    print "-" * 20
    print "Current organism: ", organism
    organism.transcribe()
    organism.translate()
    environment.population_list.append(organism.reproduce())
    print "Population:", len(environment.population_list)
    print environment.population_list
    print "-" * 20
    if len(environment.population_list) >= environment.carrying_capacity:
        break
stop = time.clock()


print environment.population_list
print "Total time taken =", (stop-start), "seconds"
