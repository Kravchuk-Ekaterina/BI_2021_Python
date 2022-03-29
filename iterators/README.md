# ITERATORS AND GENERATORS
## Task 1
Implemented a generator fasta_reader that takes the path to the fasta file as input and outputs pairs of sequence id and the sequence.
## Task 2
Implemented a class that reads sequences with some minor modifications. It works with DNA and protein fasta files. An object of this class supports iteration. In the process of iteration, the class endlessly iterates over the sequences in the file. If the file is over, then the iteration continues from its beginning. When returning each next sequence, the class slightly changes it with a given probability.<br>
The class has a constructor with the following arguments:<br>
- path: the path to the fast file<br>
- proba: probability to change the sequence (0.01 by default)<br>
- mutation: the way to change the sequence: 'substitution', 'deletion', 'insertion' or 'any' ('any' by default)<br>
The class has the following attributes:<br>
- fasta_content: a dictionary containing the information from the fasta file. IDs are keys, sequences are values.<br>
- current_id - current index for iteration<br>
- monomers: bases for DNA or aminoacids for protein fasta
It has the following methods:<br>
- __init__<br>
- __iter__<br>
- substitution: changes the base/aminoacid to another random letter with the given probability (randomly the letter can be changed to itself)<br>
- deletion: removes the base/aminoacid with the given probability<br>
- insertion: inserts a base/aminoacid with the given probability<br>
