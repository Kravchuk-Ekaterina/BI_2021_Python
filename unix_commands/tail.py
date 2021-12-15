#!/usr/bin/python3

# Importing packages
import argparse
import os
import sys

# Parsing arguments
from argparse import ArgumentParser

parser = ArgumentParser(description="tail analogue")
parser.add_argument('data', metavar = 'DATA', nargs='*', default=(None if sys.stdin.isatty() else sys.stdin.read()))
parser.add_argument('-n', '--lines_number', help='Display the last H lines, not the last 10 or use -n + H to output starting with H')
args = parser.parse_args()

n = args.lines_number
if n == None:
    n = '10'
plus = n[0]

n = int(n)
if n < 0:
    n = n * (-1)
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
            if plus != '+':
                my_out = strings[len(strings)-n:]
            else:
                my_out = strings[n-1:]

if status == 'inp':
    strings = data.split('\n')
    strings = strings[:-1]
    if plus != '+':
        my_out = strings[len(strings)-n:]
    else:
        my_out = strings[n-1:]

for i in my_out:
    print(i)
