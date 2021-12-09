#!/usr/bin/python3

# Importing packages
import argparse
import sys
import os

# Parsing arguments
from argparse import ArgumentParser

parser = ArgumentParser(description="wc analogue")
parser.add_argument('-l', '--lines', action='store_true', help="Display the number of lines in object")
parser.add_argument('-w', '--words', action='store_true', help="Display the number of words")
parser.add_argument('-c', '--bytes', action='store_true', help="Display the size of an object in bytes")
parser.add_argument('data', metavar = 'DATA', nargs='?', default=(None if sys.stdin.isatty() else sys.stdin.read()))
args = parser.parse_args()

data = args.data
status = 'inp'

if os.path.exists(data):
    status = 'f'
    with open (data, 'r') as file:
        data = file.read()
    
out = 0

if args.lines:
    lines = data.split('\n')
    out = len(lines) - 1

if args.words:
    lines = data.split('\n')
    for line in lines:
        words = line.split()
        out += len(words)
if args.bytes:
    out = sys.getsizeof(data)

if status == 'f':
    print(out, args.data)
else:
    print(out)
