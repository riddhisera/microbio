##to retrive combined files of the same strains

from Bio import Entrez
import csv

Entrez.email = "sera.1@iitj.ac.in" 

no = 1
current_strain = ""

import csv
with open('indianwholegenome_97.csv', 'r') as file:  #input file name - refer for format, check line 22
    reader = csv.reader(file)
    itercars = iter(reader)
    next(itercars)
    for row in itercars:
        if row != ['', '', '']:
            new_strain = row[2].split(' ')[row[2].split(' ').index("strain")+ 1]
            search_handle = Entrez.esearch(db="nucleotide",term=row[1], usehistory="y", idtype="acc")   #change row[index]
            search_results = Entrez.read(search_handle)
            search_handle.close()

            acc_list = search_results["IdList"] 
            webenv = search_results["WebEnv"]
            query_key = search_results["QueryKey"]

            fetch_handle = Entrez.efetch(db="nucleotide",rettype="fasta",retmode="text",webenv=webenv,query_key=query_key,idtype="acc")
            data = fetch_handle.read()

            filename = "kleb_" + str(new_strain) + ".fasta"
            write_file = open(filename, "a")
            write_file.write(data)

            print("file",no,"done")  # remove
            no+=1

