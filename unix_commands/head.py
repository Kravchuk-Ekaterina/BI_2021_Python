#!/usr/bin/python3

# Importing packages
import argparse
import os
import sys

# Parsing arguments
from argparse import ArgumentParser

parser = ArgumentParser(description="head analogue")
parser.add_argument('data', metavar = 'DATA', nargs='*', default=(None if sys.stdin.isatty() else sys.stdin.read()))
parser.add_argument('-n', '--lines_number', help='print K lines of each file, not the first 10, if K is preceded by "-", print everything except K')
args = parser.parse_args()

n = args.lines_number
if n == None:
    n = 10

n = int(n)

data = args.data
status = 'inp'
files = []

if os.path.exists(str(data[0])):
    status = 'f'
    for i in data:
        files.append(i)
my_out = []    
if status == 'f':
    for i in files:
        with open(i, 'r') as file:
            strings = file.read()
            strings = strings.split('\n')
            strings = strings[:-1]
            my_out = strings[:n]

if status == 'inp':
    strings = data.split('\n')
    strings = strings[:-1]
    my_out = strings[:n]

for i in my_out:
    print(i)
