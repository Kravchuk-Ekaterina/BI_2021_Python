#!/usr/bin/env python3

# Importing packages
import argparse
import os
import sys

# Parsing arguments
from argparse import ArgumentParser

parser = ArgumentParser(description="cat analogue")
parser.add_argument('data', metavar = 'DATA', nargs='*', default=(None if sys.stdin.isatty() else sys.stdin.read()))
args = parser.parse_args()

data = args.data
status = 'inp'
files = []

if os.path.exists(str(data[0])):
    status = 'f'
    for i in data:
        files.append(i)
     
if status == 'f':
    for i in files:
        with open(i, 'r') as file:
            strings = file.read()
            strings = strings.split('\n')
            strings = strings[:-1]
            for s in strings:
                print(s)

if status == 'inp':
    print(data)
