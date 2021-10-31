HW VIRTUAL ENVIRONMENTS

The programmer Mike was interested in virtual environments and decided to research it. After many years of research he published a paper, the code is available (https://github.com/krglkvrmn/Virtual_environment_research). However, this code is not easy to use for others...
Here you can find the instruction how to use it

The script was tested on Ubuntu 21.04, Python 3.9.7

The file requirements.txt contains a list of libraries, necessary to launch the file pain.py

The instructions:

1) Download pain.py and requirements.txt

2) If you don't have the library for creating virtual environments, install it
$ python -m pip install virtualenv

3) Create the virtual environment
$ python -m virtualenv any_name

4) Activate the virtual environment
$ source any_name_that_you_like/bin/activate

5) Install packages listed in the file requirements.txt
$ python -m pip install -r requirements.txt

6) Finally launch pain.py
