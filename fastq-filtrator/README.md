FASTG-FILTRATOR FOR OPERATIONS WITH FASTQ-FILES

Functions of the program:

- Filter reads based on GC-content
- Filter reads based on length
- Filter reads based on quality (Q-score)
- Save filtered reads to file
- 
The function main() has the following arguments:

- input_fastq - the path to file .fatstq
- output_file_prefix - prefix to output files ("_passed.fastq" will be added to output with correct reads and "_failed.fastq" for output with filtered reads (only if the argument save_filtered is True)
- gc_bounds - interval* of GC-content (per cent) for filtration (default = (0, 100), i.e. all reads preserved). If one number is given, it is the upper bound.
- length_bounds - interval* of read length (nucleotides) for filtration (default = (0, 2^32)). If one number is given, it is the upper bound.
- quality_threshold - the threshold for mean value of nucleotide quality (scale phred 33)
- save_filtered - whether the program should save filtered (default = False)
