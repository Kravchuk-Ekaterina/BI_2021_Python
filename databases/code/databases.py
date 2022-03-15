# DATABASES
import pandas as pd
import sqlite3

# Observing data
metadata = pd.read_csv('../data/metadata.csv')
metadata.info()
genstudio = pd.read_csv('../data/genstudio.csv')
genstudio.info()

# Creating the database and its structure
connection = sqlite3.connect('genotyping_data.db')

metadata_query = '''CREATE TABLE metadata(
                                 metadata_id INTEGER PRIMARY KEY,
                                 dna_chip_id TEXT,
                                 breed TEXT,
                                 sex TEXT)'''
connection.execute(metadata_query)

genstudio_query = '''CREATE TABLE genstudio(
                                  genstudio_id INTEGER PRIMARY KEY,
                                  SNP_Name TEXT,
                                  SNP_Index INTEGER,
                                  SNP_Aux INTEGER,
                                  Sample_ID TEXT,
                                  SNP TEXT,
                                  Allele1_Top TEXT,
                                  Allele2_Top TEXT,
                                  Allele1_Forward TEXT,
                                  Allele2_Forward TEXT,
                                  Allele1_AB TEXT,
                                  Allele2_AB TEXT,
                                  Chr TEXT,
                                  Position TEXT,
                                  GC_Score REAL,
                                  GT_Score REAL,
                                  Theta REAL,
                                  R REAL,
                                  B_Allele_Freq REAL,
                                  Log_R_Ratio REAL)'''
connection.execute(genstudio_query)

# Inserting data to the tables
metadata_list = metadata.drop('Unnamed: 0', axis = 1).values.tolist()
genstudio_list = genstudio.drop('Unnamed: 0', axis = 1).values.tolist()

metadata_insertion_query = '''INSERT INTO
                                 metadata(dna_chip_id, breed, sex)
                                 VALUES(?, ?, ?)'''

connection.executemany(metadata_insertion_query, metadata_list)
connection.commit()

genstudio_insertion_query = genstudio_query = '''INSERT INTO
                                  genstudio(
                                  SNP_Name, 
                                  SNP_Index, 
                                  SNP_Aux, 
                                  Sample_ID, 
                                  SNP, 
                                  Allele1_Top, 
                                  Allele2_Top, 
                                  Allele1_Forward,
                                  Allele2_Forward,
                                  Allele1_AB,
                                  Allele2_AB,
                                  Chr,
                                  Position,
                                  GC_Score,
                                  GT_Score,
                                  Theta,
                                  R,
                                  B_Allele_Freq,
                                  Log_R_Ratio)
                                  VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                  '''

connection.executemany(genstudio_insertion_query, genstudio_list)
connection.commit()

# Requests to the database
select_metadata_query = '''SELECT dna_chip_id, breed, sex
                                 FROM metadata'''

connection.execute(select_metadata_query).fetchall()

select_genstudio_query = '''SELECT SNP_Name, SNP, Chr, Position
                                 FROM genstudio'''

connection.execute(select_genstudio_query).fetchall()

# Closing connection
connection.close()