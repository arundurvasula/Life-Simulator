from organism import Organism
from environment import Environment
from sys import argv
import time

# what a mess.

# filename = argv[1]
# fasta = open(filename,"r")
# 
# 
# def parse_fasta(filename):
#     sequence = ""
#     for line in filename:
#         if (not line.startswith(">")):
#             sequence = sequence + line
#     
#     sequence.replace("\n", "")
#     return sequence
#             
# sequence = parse_fasta(fasta)
environment = Environment(0.042, 10)
organism = Organism("GTCGATCGATCGATCGATCGATCGGTC") 
environment.population_list.append(organism)

def mutate_everyone():
    print environment.mutate(environment.population_list[0].DNA)
    environment.mutate_population()
    print environment.mutate(environment.population_list[0].DNA)
	
def mutate_individual():
    #mutates individual 1
    for org in environment.population_list:
        if len(environment.population_list) >= environment.carrying_capacity:
            break
        org.transcribe()
        org.translate()
        environment.population_list.append(org.reproduce())
        
    environment.population_list[1].DNA = environment.mutate(environment.population_list[1].DNA)
    
    for org in environment.population_list:
        print org.DNA
		
mutate_individual()
        
