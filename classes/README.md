# BI_2021_Python
## Task 1
Created class Snail describing snails :3 <br>
 - Such objects have names, species, age (in months) and size (in mm) and status. Status stores the information if the snail is hidding from the world or not.<br>
 - Method age_group gives you the age group of the snail using the information stired in age. There are 3 age groups: young, adult and old.<br>
 - Method size_group gives you the size group of the snail using the information stired in size. There are 3 size groups: small, medium and large.<br>
 - Method growth helps to increase the snail's size.<br>
 - Method greet shows you the snail's greeting.<br>
## Task 2
Created a class describing RNA which:
 - Gets the RNA sequence and creates an object with it
 - Has the methon translation to get the protein using the genetic code
 - Has the method reverse_transcription to get the complementary DNA sequence
## Task 3
I wrote a class, inheriting from sets, which contains only positive numbers when created and will not add non-positive elements
## Task 4
Creating class for collecting statistics on .fasta.
### Input parameters:
- Path to .fasta file
### Methods:
- Counting the number of sequences in a .fasta file<br>
- Building a histogram of sequence lengths<br>
- Calculation of GC-content<br>
- Building a histogram of the frequency of k-mers (on the x-axis each of the possible k-mers, and on the y-axis - their frequency). Additionaly: building a histogram of the frequency of 4-mers<br>
- Override method for printing information (enough text indicating the path to the file)<br>
- Execution of all used methods for calculating metrics<br>
