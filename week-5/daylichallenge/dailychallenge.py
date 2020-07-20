import ramdom



class Gene():
    def __init__(self):
        self.value= random.choice([True ,False])# accept a list of arguments

    def mutate(self):
        self.value = not  self.value

    def __repr__(self):
        return "1" if self.value else "0"


g1= Gene()
g1.value





class Chromosome:
    def __init__(self):
        self.value = [Gene() for i in range (10)]

    def mutate (self):
        for gene in self.value:
            if random.choice([True, False]):
                gene.mutate()

    def __repr__(self):
        return str(self.value)


class DNA():
    def __init__(self):
        self.value = [Chromosome()for i in range (10)]


    def mutate (self):
        for Chromosome in self.value:
            if random.choice([True, False]):
                Chromosome.mutate()

    def __repr__(self):
        return str(self.value)


class  Organism():
    def __ init__(self,dna, probability_to_mutate ):
    self.dna= dna
    self.probability_to_mutate= probability_to_mutate

    def mutate(self):
        if random.random() <=  self.probability_to_mutate:
            self.dna.mutate()

    def __repr__(self):
        return str (self.dna)

class Evolution():
    def __init__(self,num_of_organism):
        self.population = [Organism(DNA(),0.8) for i in range (num_of_organism)]
        self.generations = 0




    def big_bang(self):
        for organism in self.population:
            organism.mutate()



















