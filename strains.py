#to get list of unique strains from the csv file

from Bio import Entrez
import csv

Entrez.email = "sera.1@iitj.ac.in" 

no = 1
strains = []
filename = "indianKlebStrains58.txt"

import csv
with open('indCompletegenome_60.csv', 'r') as file:  #input file name - refer for format, check line 22
    reader = csv.reader(file)
    itercars = iter(reader)
    next(itercars)
    for row in itercars:
        if row != []:
            new_strain = row[2].split(' ')[row[2].split(' ').index("strain")+ 1]
            write_file = open("all.txt", "a")
            write_file.write(new_strain)
            write_file.write("\n")
            if new_strain in strains:
                None
            else:         
                write_file = open(filename, "a")
                write_file.write(new_strain)
                write_file.write("\n")
                strains.append(new_strain)



