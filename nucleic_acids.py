# We should check if the sequence is nucleic acid

def is_dna(x):    
    bases = ['a', 'c', 't', 'g', 'A', 'C', 'T', 'G']
    for i in range(len(x)):    
        answer = True
        if i not in bases:    
            answer = False
            break
    return answer

def is_rna(x):    
    bases = ['a', 'c', 'u', 'g', 'A', 'C', 'U', 'G']
    for i in range(len(x)):    
        answer = True
        if i not in bases:    
            answer = False
            break
    return answer

# Let's create the dictionary of complement pairs

dna_pairs = {'A':'T', 'G':'C', 'T':'A', 'C':'G', 'a':'t', 't':'a', 'g':'c', 'c':'g'}

rna_pairs = {'A':'U', 'U':'A', 'C':'G', 'G':'C', 'a':'u', 'u':'a', 'g':'c', 'c':'g'}

