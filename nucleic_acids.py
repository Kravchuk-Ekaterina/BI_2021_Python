# Check if the sequence is nucleic acid


def is_dna(x):
    bases = {'a', 'c', 't', 'g', 'A', 'C', 'T', 'G'}
    return set(x) <= bases


def is_rna(x):
    bases = {'a', 'c', 'u', 'g', 'A', 'C', 'U', 'G'}
    return set(x) <= bases


# Transcribe


def transcribe(x):
    dna_to_rna = {'A': 'U', 'a': 'u', 'T': 'A', 't': 'a', 'G': 'C', 'g': 'c', 'C': 'G', 'c': 'g'}
    transcript = []
    for i in x:    
        transcript.append(dna_to_rna[i])
    print("".join(transcript))

    
"""
В примере из задания просто T  заменяется на U, тогда функция должна была выглядеть так, но в итоге я решила использовать другую версию

def transcribe(x):    
    transcript = x.replace('T', 'U')
    transcript = transcript.replace('t', 'u')
    print(transcript)
"""


# Complement

def complement(x):
    seq = ''
    dna_pairs = {'A': 'T', 'T': 'A', 'a': 't', 't': 'a', 'G': 'C', 'C': 'G', 'g': 'c', 'c': 'g'}
    rna_pairs = {'A': 'U', 'U': 'A', 'a': 'u', 'u': 'a', 'G': 'C', 'C': 'G', 'g': 'c','c': 'g'}
    if is_dna(x):    
        pairs = dna_pairs
    else:    
        pairs = rna_pairs
    for i in x:    
        seq += pairs[i]
    print(seq)

    
# Reverse complement


def reverse_complement(x):
    seq = x[::-1]
    complement(seq)

    
# Count bases


def bases_count(x):
    x = x.upper()
    print('A:', x.count('A'))
    print('G:', x.count('G'))
    print('C:', x.count('C'))
    if is_rna(x):    
        print('U:', x.count('U'))
    else:    
        print('T:', x.count('T'))

        
# Base content


def base_perc(x):
    x = x.upper()
    n = len(x)
    print('A:', x.count('A')/n)
    print('G:', x.count('G')/n)
    print('C:', x.count('C')/n)
    if is_rna(x):    
        print('U:', x.count('U')/n)
    else:    
        print('T:', x.count('T')/n)

        
# gc content


def gc(x):
    x = x.upper()
    g = x.count('G')
    c = x.count('C')
    n = len(x)
    print((g + c)/n)

    
# the cycle


commands = {'exit', 'transcribe', 'reverse', 'complement', 'reverse complement', 'count bases', 'base content', 'gc content'}

while True:
    command = input('Enter command:')
    if command == 'exit':    
        print('Good luck')
        break
    if command not in commands:    
        print('Try again!')
    else:   
        sequence = input('Enter sequence:')
        while ((not is_dna(sequence)) and (not is_rna(sequence))):    
            print('Try again!')
            sequence = input('Enter sequence:')
        if command == 'transcribe':    
            while not is_dna(sequence):    
                print('Try again!')
                sequence = input('Enter sequence:')
            transcribe(sequence)
        elif command == 'reverse':    
            print(sequence[::-1])
        elif command == 'complement':    
            complement(sequence)
        elif command == 'reverse complement':    
            reverse_complement(sequence)
        elif command == 'count bases':    
            bases_count(sequence)
        elif command == 'base content':    
            while sequence == '':    
                print('The input is empty. Try again!')
                sequence = input('Enter sequence:')
            base_perc(sequence)
        elif command == 'gc content':
            while sequence == '':    
                print('The input is empty. Try again!')
                sequence = input('Enter sequence:')
            gc(sequence)
