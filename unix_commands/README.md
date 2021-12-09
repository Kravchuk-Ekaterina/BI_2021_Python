# os and sys modules homework
## Functionality
I implemented programs that mimic UNIX utilities. <br>
Each program is in a separate script, which are named by the template utility_name.py. That is, the analogue of wc will be called wc.py, grep - grep.py, etc.<br>
Like the reference utilities, these utilities are able to accept an argument or stream as input.<br>
The utilities are able to work in pipelines with each other and with UNIX utilities.<br>
I implemented: <br>
1) wc.py which mimics wc with options -l -w- c <br>

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

