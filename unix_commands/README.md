# os and sys modules homework
## Functionality
I implemented programs that mimic UNIX utilities. <br>
Each program is in a separate script, which are named by the template utility_name.py. That is, the analogue of wc will be called wc.py, grep - grep.py, etc.<br>
Like the reference utilities, these utilities are able to accept an argument or stream as input.<br>
The utilities are able to work in pipelines with each other and with UNIX utilities.<br>
I implemented: <br>
1) wc.py which mimics wc with options -l -w -c <br>
2) ls.py which mimics ls with option -a <br>
3) sort.py which mimics sort <br>
4) rm.py which mimics rm with option -r<br>
5) cat.py which mimics cat<br>

## Usage
### 1) Create and activate a virtual environment and use the python interpreter from the currently active environment
```bash
conda create -n environment_name python
```
When conda asks you to proceed, type y
```bash
proceed ([y]/n)?
```
This creates the environment_name environment in /envs/.<br>
Activate the environment:
```bash
conda activate environment_name
```
If you want to deactivate the environment use the command:
```bash
conda deactivate
```
### 2) Dowload the utilities
Download utility_name.py to your working directory<br>
Make all the scripts executable. Use the following command:
```bash
chmod +x ./utility_name.py
```
### 3) Usage of the specific utilities
#### wc.py
the utility is wc analogue <br>
to use is start the command with ./wc.py <br>
Use the following command to get the help message:
```bash
./wc.py -h
```
or 
```bash
./wc.py --help
```
Here is the help message:
```bash
usage: wc.py [-h] [-l] [-w] [-c] [DATA]

wc analogue

positional arguments:
  DATA

optional arguments:
  -h, --help   show this help message and exit
  -l, --lines  Display the number of lines in object
  -w, --words  Display the number of words
  -c, --bytes  Display the size of an object in bytes
```
Some examples of usage:
```bash
./wc.py -c ./test_data/test.fastq
```
The output:<br>
127775335 ./test_data/test.fastq
```bash
head ./test_data/test.fastq | ./wc.py -l
```
The output:<br>
10
#### ls.py
the utility is ls analogue <br>
to use is start the command with ./ls.py <br>
Use the following command to get the help message:
```bash
./ls.py -h
```
or
```bash
./ls.py --help
```
Here is the help message:
```bash
usage: ls.py [-h] [-a] [PATH]

ls analogue

positional arguments:
  PATH

optional arguments:
  -h, --help  show this help message and exit
  -a, --all   Do not hide files starting with .
```
Some examples of usage:
```bash
./ls.py ../
```
The output:<br>
fastq_filtrator virtual_environment numpy_challenge unix_commands README.md units_converter nucleic_acids
```bash
./ls.py -a
```
The output:<br>
ls.py .test README.md wc.py test_data
#### sort.py
the utility is sort analogue <br>
to use is start the command with ./sort.py <br>
Use the following command to get the help message:
```bash
./sort.py -h
```
or
```bash
./sort.py --help
```
Here is the help message:
```bash
usage: sort.py [-h] [DATA ...]

sort analogue

positional arguments:
  DATA

optional arguments:
  -h, --help  show this help message and exit
```
Some examples of usage (the used data you can find in ./test_data/Test_for_sort/):
```bash
./sort.py ./test_data/test_for_sort/file1.txt ./test_data/test_for_sort/file2.txt ./test_data/test_for_sort/new_file.txt
```
The output:<br>
<br>
<br>
1<br>
16<br>
2<br>
3<br>
8<br>
another text<br>
more text<br>
new_text<br>
some text<br>
```bash
cat ./test_data/test_for_sort/file1.txt | ./sort.py
```
The output:<br>
<br>
1<br>
16<br>
3<br>
some text<br>
#### rm.py
the utility is rm analogue <br>
to use is start the command with ./rm.py <br>
Use the following command to get the help message:
```bash
./rm.py -h
```
or
```bash
./rm.py --help
```
Here is the help message:
```bash
usage: rm.py [-h] [-r] [PATH ...]

rm analogue

positional arguments:
  PATH

optional arguments:
  -h, --help           show this help message and exit
  -r, -R, --recursive  Recursively delete directories and their contents
```
Some examples of usage (the used data you can find in ./test_data/Test_for_sort/):
```bash
./rm.py test_file test_dir imagination.txt
```
The output:<br>
It is impossible to remove test_dir. It is a directory.<br>
You tried to remove imagination.txt. It is impossible. There is no such file or directory.<br>
test_file is removed
```bash
./rm.py -r test_file test_dir imagination.txt
```
The output:<br>
You tried to remove test_file. It is impossible. There is no such file or directory.<br>
You tried to remove imagination.txt. It is impossible. There is no such file or directory.<br>
test_dir is removed
#### cat.py
the utility is cat analogue <br>
to use is start the command with ./cat.py <br>
Use the following command to get the help message:
```bash
./cat.py -h
```
or
```bash
./cat.py --help
```
Here is the help message:
```bash
usage: cat.py [-h] [DATA ...]

cat analogue

positional arguments:
  DATA

optional arguments:
  -h, --help  show this help message and exit
```
Some examples of usage (the used data you can find in ./test_data/Test_for_sort/):
```bash
./cat.py ./test_data/test_for_sort/file1.txt ./test_data/test_for_sort/file2.txt
```
The output:<br>
1<br>
3<br>
16<br>
<br>
some text<br>
2<br>
8<br>
another text<br>
<br>
more text<br>
```bash
head ./test_data/test.fastq | ./cat.py
```
The output:<br>:
@SRR1363257.37 GWZHISEQ01:153:C1W31ACXX:5:1101:14027:2198 length=101<br>
GGTTGCAGATTCGCAGTGTCGCTGTTCCAGCGCATCACATCTTTGATGTTCACGCCGTGGCGTTTAGCAATGCTTGAAAGCGAATCGCCTTTGCCCACACG<br>
+<br>

