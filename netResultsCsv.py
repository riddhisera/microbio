## retrive results from NCBI and write it to a csv file

import csv

from Bio import Entrez
Entrez.email = "sera.1@iitj.ac.in" # Always tell NCBI who you are
handle = Entrez.egquery(term="Klebsiella pneumoniae")
record = Entrez.read(handle)

count = 60     # for complete result, change it to 570
handle = Entrez.esearch(db="nucleotide", term="Klebsiella pneumoniae AND \"complete genome\" AND India AND (\"3000000\"[SLEN] : \"8000000\"[SLEN]))", retmax=count)
record = Entrez.read(handle)
gi_list = record["IdList"]

number = 0

fields = ['Sno','Accession ID','Description'] 
filename = "indCompletegenome_60.csv"   #change file name if needed
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile, dialect='excel') 
    csvwriter.writerow(fields)

    for ide in gi_list:
        handle = Entrez.efetch(db="nucleotide", id=ide, rettype="gb", retmode="text") 
        data = handle.read()
        words = data.split()
        x = int(words.index('ACCESSION'))
        y = int(words.index('VERSION'))
        acc_number = words[y+1]
        description = ' '.join(words[9:x])
        number += 1
        row = [number,acc_number,description]
        print(number)
        csvwriter.writerow(row)

