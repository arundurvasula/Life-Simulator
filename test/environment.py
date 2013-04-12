import random
import math
import sys

class Environment(object):
    
    def __init__(self, mutation_rate=0, carrying_capacity=500):
        self.mutation_rate = mutation_rate
        self.carrying_capacity = carrying_capacity
        self.population_list = []
        
    def mutate(self, DNA):
        """Return the mutated DNA string. This function randomly chooses to do either
        a substitution or frameshift mutation.
        """
        #strings are immutable so I have to turn DNA into a list first. 
        list_DNA = list(DNA) 
        
        mutation_dict = { 0:"substitution",
                          1:"frame_shift" }
        bp_dict = { 0:"A", 1:"T", 2:"C", 3:"G" }
        
        # number of times to mutate
        if self.mutation_rate > 0:
            mutate_number = math.floor(self.mutation_rate * (len(DNA) - 1))
        elif self.mutation_rate == 0:
            sys.exit("Mutate called when mutation_rate == 0.")
        i = 0 #for use in the while loop below
        
        # random variables
        base_pair = bp_dict[random.randint(0, 3)]
        mutation_location = random.randint(0, (len(DNA) - 1)) #adjust for 0 based counting
        mutation_type = random.randint(0, 1)

        while i < mutate_number:
            if mutation_type == 0:
                #substitution
                #print mutation_dict[mutation_type] , "at" , mutation_location
                #print "substituting", list_DNA[mutation_location], "with", base_pair
                list_DNA[mutation_location] = base_pair
                
            elif mutation_type == 1:
                #frame_shift
                indel = random.randint(0, 1)
                if indel == 0:
                    #insert
                    list_DNA.insert(mutation_location, base_pair)
                elif indel == 1:
                    #deletion
                    del list_DNA[mutation_location]        
            else: 
            	sys.exit("Random number error. Check the code, yo.")
            i += 1
        
                   
        DNA = "".join(list_DNA)
        return DNA
        
    def mutate_population(self):
        """Runs through the population and mutates it."""
        for key in self.population_list:
            key.DNA = self.mutate(key.DNA) # pass organism.DNA because mutate needs it
