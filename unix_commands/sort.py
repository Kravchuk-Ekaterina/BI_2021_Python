#!/usr/bin/env python3

# Importing packages
import argparse
import os
import sys

# Parsing arguments
from argparse import ArgumentParser

parser = ArgumentParser(description="sort analogue")
parser.add_argument('data', metavar = 'DATA', nargs='*', default=(None if sys.stdin.isatty() else sys.stdin.read()))
args = parser.parse_args()

data = args.data
status = 'inp'
files = []

if os.path.exists(str(data[0])):
    status = 'f'
    for i in data:
        files.append(i)
     
for_sorting = []
if status == 'f':
    for i in files:
        with open(i, 'r') as file:
            strings = file.read()
            strings = strings.split('\n')
            strings = strings[:-1]
            for s in strings:
                for_sorting.append(s)

if status == 'inp':
    strings = data.split('\n')
    strings = strings[:-1]
    for s in strings:
        for_sorting.append(s)

out = sorted(for_sorting)

for a in out:
    print(a)
