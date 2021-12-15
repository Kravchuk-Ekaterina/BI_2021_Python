#!/usr/bin/env python3

# Importing packages
import argparse
import os
import shutil

# Parsing arguments
from argparse import ArgumentParser

parser = ArgumentParser(description="rm analogue")
parser.add_argument('-r', '-R', '--recursive', action='store_true', help="Recursively delete directories and their contents")
parser.add_argument('path', metavar = 'PATH', nargs='*', default = 'no path')
args = parser.parse_args()

my_path = args.path

if my_path == 'no path':
    print('You should provide the path to the file or directory')
else:
    if args.recursive:
        for i in my_path:
            if os.path.isfile(i) or os.path.isdir(i):
                shutil.rmtree(i)
            else:
                print('You tried to remove ', i, '. It is impossible. There is no such file or directory.', sep = '')
    else:
        for i in my_path:
            if os.path.isfile(i):
                os.remove(i)
            elif os.path.isdir(i):
                print('It is impossible to remove ', i, '. It is a directory.', sep = '')
            else:
                print('You tried to remove ', i, '. It is impossible. There is no such file or directory.', sep = '')

