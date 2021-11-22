# fastq-filtrator

Here I implement a program to work with fastq files.


The program is able to:
1. Filter reads by GC content
2. Filter reads by quality
3. Filter reads by length
4. Save results to file


The script file is named fastq_filtrator.py.

Realized the function main, which takes the following arguments:
1. input_fastq - path to input file
2. output_file_prefix - prefix to path to output file. "_passed.fastq" is added to the file with reads which passed filtration and "_failed.fastq" for files which did not pass (only if the argument save_filtered is True).
3. gc_bounds - interval of GC content (in percent) for filtration (by default, it is equal to (0, 100), i.e. all reads are saved). If the argument is one number it is taken as the upper bound.
4. length_bounds - interval of lenghth for filtration, by default it is (0, 2**32). If the argument is one number it is taken as the upper bound.
5. quality_threshold - threshold value of average read quality for filtering, by default it is equal to 0 (phred33 scale). Reads with an average quality for all nucleotides below the threshold are discarded
6. save_filtered - saving reads which did not pass filtration, False by default.

