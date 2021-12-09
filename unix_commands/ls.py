#!/usr/bin/python3

# Importing packages
import argparse
import os

# Parsing arguments
from argparse import ArgumentParser

parser = ArgumentParser(description="ls analogue")
parser.add_argument('-a', '--all', action='store_true', help="Do not hide files starting with .")
parser.add_argument('path', metavar = 'PATH', nargs='?', default='./')
args = parser.parse_args()

my_path = args.path

files = os.listdir(my_path)
files_no_dot = []

if args.all:
    print(' '.join(files))
else:
    for f in files:
        if f[0] != '.':
            files_no_dot.append(f)
    print(' '.join(files_no_dot))
