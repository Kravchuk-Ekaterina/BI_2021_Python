# Importing packages

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# GenscanOutput class

class GenscanOutput:
    def __init__(self, status, cds_list, intron_list, exon_list):
        self.status = status
        self.cds_list = cds_list
        self.intron_list = intron_list
        self.exon_list = exon_list

# run_genscan function

def run_genscan(sequence=None, sequence_file=None, organism="Vertebrate",exon_cutoff=1.00, sequence_name="", print_options='Predicted peptides only'):
    
    form_url = 'http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi'

    if sequence_file is not None:
        with open(sequence_file, "rb") as sequence_file:
            files = {'-u': sequence_file}

            payload = {
                '-o': organism,
                '-e': exon_cutoff,
                '-n': sequence_name,
                '-p': print_options,
            }

            resp = requests.post(form_url, data=payload, files=files)

    else:
        payload = {
            '-o': organism,
            '-e': exon_cutoff,
            '-n': sequence_name,
            '-p': print_options,
            '-s': sequence
        }

        resp = requests.post(form_url, data=payload)
        
    status = resp.status_code

    soup = str(BeautifulSoup(resp.content).find('pre').text)

    # peptides
    peptides = []

    for peptide in re.compile(r'aa\n[A-Y\n]+').findall(soup):
        peptides.append(peptide[2:].replace('\n', ''))

    # exons
    exon_start = []
    exon_end = []

    for exon in re.compile(r'1\.\d\d.+\d').findall(soup):
        exon_start.append(int(exon[11:18]))
        exon_end.append(int(exon[18:25]))
    
    exons = pd.DataFrame({'exon start':exon_start, 'exon end':exon_end}, columns  = ['exon start', 'exon end'])

    # introns
    intron_start = [0]
    intron_end = []
    length = int(re.compile(r'fasta.+bp').findall(soup)[0][7:-2])

    for i in range(len(exon_start)):
        intron_end.append(exon_start[i]-1)
        intron_start.append(exon_end[i]+1)
        
    intron_end.append(length)
    
    introns = pd.DataFrame({'intron start':intron_start, 'intron end':intron_end}, columns = ['intron start', 'intron end'])

    return GenscanOutput(status = status, cds_list = peptides, intron_list = introns, exon_list = exons)
