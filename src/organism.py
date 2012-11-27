class Organism(object):

    def __init__(self, DNA):
        self.DNA = DNA.upper()
        self.RNA = ""
        self.proteins = ""
        self.genes = {} #this dict holds the gb and extra information; not implemented
        
    def transcribe(self):
        """Creates a string RNA which holds mRNA information from DNA."""
        for i in self.DNA:
            if i == "A":
                self.RNA += "A"
            elif i == "C":
                self.RNA += "C"
            elif i == "T":
                self.RNA += "U"
            elif i == "G":
                self.RNA += "G"
                
        return self.RNA
        
    def translate(self):
        """Creates a string of proteins from the mRNA data."""
        self.list_RNA = list(self.RNA) #turned into a list for iteration
        self.end = len(self.list_RNA) #how far to iterate
        self.RNA_codes = {
                            "UUU":"F",
                            "UUC":"F",
                            "UUA":"L",
                            "UUG":"L",
                            "CUU":"L",
                            "CUC":"L",
                            "CUA":"L",
                            "CUG":"L",
                            "AUU":"I",
                            "AUC":"I",
                            "AUA":"I",
                            "AUG":"M",
                            "GUU":"V",
                            "GUC":"V",
                            "GUA":"V",
                            "GUG":"V",
                            "UCU":"S",
                            "UCC":"S",
                            "UCA":"S",
                            "UCG":"S",
                            "CCU":"P",
                            "CCC":"P",
                            "CCA":"P",
                            "CCG":"P",
                            "ACU":"T",
                            "ACC":"T",
                            "ACA":"T",
                            "ACG":"T",
                            "GCU":"A",
                            "GCC":"A",
                            "GCA":"A",
                            "GCG":"A",
                            "UAU":"Y",
                            "UAC":"Y",
                            "UAA":".",
                            "UAG":".",
                            "CAU":"H",
                            "CAC":"H",
                            "CAA":"Q",
                            "CAG":"Q",
                            "AAU":"N",
                            "AAC":"N",
                            "AAA":"K",
                            "AAG":"K",
                            "GAU":"D",
                            "GAC":"D",
                            "GAA":"E",
                            "GAG":"E",
                            "UGU":"C",
                            "UGC":"C",
                            "UGA":".",
                            "UGG":"W",
                            "CGU":"R",
                            "CGC":"R",
                            "CGA":"R",
                            "CGG":"R",
                            "AGU":"S",
                            "AGC":"S",
                            "AGA":"R",
                            "AGG":"R",
                            "GGU":"G",
                            "GGC":"G",
                            "GGA":"G",
                            "GGG":"G" }
                                                
        for i in xrange(0, self.end, 3): #loops over string every 3 bases
            try:
                #create the triplet code out of the RNA every iteration
                self.triplet = (self.list_RNA[i] + self.list_RNA[i+1] + 
                                self.list_RNA[i+2]) 
            except IndexError:
                print "Warning: Inputted DNA sequence was not divisible by 3.",
                print "Some information may have been lost."
            for key in self.RNA_codes:
                if self.triplet == key:
                    self.proteins += self.RNA_codes[key]
                    
        return self.proteins
    
   
    def reproduce(self):
        return Organism(self.DNA)
    
        
         
            
            
