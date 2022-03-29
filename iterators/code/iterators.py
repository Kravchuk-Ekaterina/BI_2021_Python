import numpy as np

# Task 1

def fasta_reader(path):
    id_, seq = None, ''
    fasta_content = []
    with open(path) as file:
        for line in file:
            fasta_content.append(line.rstrip())
    for line in fasta_content:
        if line.startswith(">"):
            if id_: yield (id_, seq)
            id_, seq = line, ''
        else:
            seq += line
    if id_: yield (id_, seq)

# Task 2

class FastaMutator:
    
    def __init__(self, path, proba=0.01, mutation='any'):
        self.path = path
        self.proba = proba
        self.mutation = mutation
        self.fasta_content = {}
        self.current_id = -1
        for id_, seq in fasta_reader(path):
            self.fasta_content[id_] = seq
        self.monomers = ['A', 'T', 'G', 'C']
        for i in list(self.fasta_content.values())[0]:
            if i not in self.monomers:
                self.monomers = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'X']
        if self.mutation == 'substitution':
            self.substitution()
        elif self.mutation == 'deletion':
            self.deletion()
        elif self.mutation == 'insertion':
            self.insertion()
        else:
            self.any_mutation()
        
    def substitution(self):
        for id_ in self.fasta_content:
            seq = self.fasta_content[id_]
            outcome = np.random.uniform()
            if outcome <= self.proba:
                seq = list(seq)
                position = np.random.randint(len(seq)+1)
                seq[position] = np.random.choice(monomers)
                self.fasta_content[id_] = ''.join(seq)
    
    def deletion(self):
        for id_ in self.fasta_content:
            seq = self.fasta_content[id_]
            outcome = np.random.uniform()
            if outcome <= self.proba:
                seq = list(seq)
                position = np.random.randint(len(seq)+1)
                seq[position] = '-'
                seq = ''.join(seq)
                self.fasta_content[id_] = seq.replace('-', '')
    
    def insertion(self):
        for id_ in fasta_content:
            seq = fasta_content[id_]
            outcome = np.random.uniform()
            if outcome <= self.proba:
                seq = list(seq)
                position = np.random.randint(len(seq)+1)
                seq[position] = seq[position] + '-'
                seq = ''.join(seq)
                self.fasta_content[id_] = seq.replace('-', np.random.choise(monomers))

    def any_mutation(self):
        for id_ in self.fasta_content:
            seq = self.fasta_content[id_]
            outcome = np.random.uniform()
            if outcome <= self.proba:
                seq = list(seq)
                mut = np.random.choice(['sub', 'del', 'ins'])
                if mut == 'sub':
                    position = np.random.randint(len(seq)+1)
                    seq[position] = np.random.choice(monomers)
                    self.fasta_content[id_] = ''.join(seq)
                elif mut == 'del':
                    position = np.random.randint(len(seq)+1)
                    seq[position] = '-'
                    seq = ''.join(seq)
                    self.fasta_content[id_] = seq.replace('-', '')
                else:
                    position = np.random.randint(len(seq)+1)
                    seq[position] = seq[position] + '-'
                    seq = ''.join(seq)
                    self.fasta_content[id_] = seq.replace('-', np.random.choise(monomers))
            
    def __iter__(self):
        return self
    
    def __next__(self):
        self.current_id += 1
        if self.current_id == len(self.fasta_content):
            self.current_id = 0
            if self.mutation == 'substitution':
                self.substitution()
            elif self.mutation == 'deletion':
                self.deletion()
            elif self.mutation == 'insertion':
                self.insertion()
            elif self.mutation == 'any':
                self.any_mutation()
            else:
                raise MutationTypeError
        return list(self.fasta_content.items())[self.current_id]