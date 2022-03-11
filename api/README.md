# API progect
The goal is to create API for the service GENSCAN http://hollywood.mit.edu/GENSCAN.html<br>
It is able to find and cut introns in the nucleotide sequence. It doesn't have a public API.
## run_genscan function
I realized the function run_genscan(sequence=None, sequence_file=None, organism="Vertebrate", exon_cutoff=1.00, sequence_name="")<br>
It executes a request similar to filling out a form on a website. It accepts as input all the parameters that can be specified on the site (except Print options):<br> 
- sequence - sequence in the form of a string or any type convenient for you, 
- sequence_file - path to a file with a sequence that will be loaded and used instead of sequence.
The function returns an object of type GenscanOutput
## GenscanOutput type
I implemented the GenscanOutput class with the following attributes:<br>
- status - request status<br>
- cds_list - list of predicted protein sequences considering splicing<br>
- intron_list - list of found introns<br>
- exon_list - list of found exons
## test data
As test data I used the sequence of tumor protein p53 TP53 (https://www.ncbi.nlm.nih.gov/gene/7157) ./test_data/TP53.fna
