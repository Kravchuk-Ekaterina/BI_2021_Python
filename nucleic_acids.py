# Check if the sequence is nucleic acid

def is_dna(x):    
    bases = ['a', 'c', 't', 'g', 'A', 'C', 'T', 'G']
    answer = True
    for i in x:    
        if i not in bases:    
            answer = False
    return answer

def is_rna(x):    
    bases = ['a', 'c', 'u', 'g', 'A', 'C', 'U', 'G']
    answer = True
    for i in x:    
        if i not in bases:    
            answer = False
    return answer

def is_nucleic_acid(x):    
    answer = False
    if is_dna(x):    
        answer = True
    elif is_rna(x):    
        answer = True
    return answer

# Transcribe

def transcribe(x):    
    transcript = x.replace('T', 'U')
    transcript = transcript.replace('t', 'u')
    print(transcript)

# Complement

def complement(x):
    seq = ''
    dna_pairs = {'A':'T', 'T':'A', 'a':'t', 't':'a', 'G':'C', 'C':'G', 'g':'c', 'c':'g'}
    rna_pairs = {'A':'U', 'U':'A', 'a':'u', 'u':'a', 'G':'C', 'C':'G', 'g':'c','c':'g'}
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

# the cycle

commands = ['exit', 'transcribe', 'reverse', 'complement', 'reverse complement']

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

