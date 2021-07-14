##total strains

from Bio import Entrez
import csv

Entrez.email = "sera.1@iitj.ac.in" 

no = 1
strains = []
filename = "indianKlebStrains.txt"

import csv
with open('indianwholegenome_570.csv', 'r') as file:  #input file name - refer for format, check line 22
    reader = csv.reader(file)
    itercars = iter(reader)
    next(itercars)
    for row in itercars:
        if row != ['', '', '']:
            new_strain = row[2].split(' ')[3]
            if new_strain in strains:
                None
            else:         
                write_file = open(filename, "a")
                write_file.write(new_strain)
                write_file.write("\n")
                strains.append(new_strain)



