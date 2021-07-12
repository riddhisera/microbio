##to retrieve the individual genome as seperate files from the queries in csv input (in fasta/txt format)

from Bio import Entrez
import csv

## creates file names
files = []
k = 1
while k < 6: # change 6 according to the number of results in the csv file
    files.append("kleb"+str(k)+".txt")  # files created would be named "kleb1.txt","kleb2.txt" etc
    k+=1

Entrez.email = "sera.1@iitj.ac.in" 

no = 0

import csv
with open('wholegenome_100.csv', 'r') as file:  #input file name - refer for format, check line 22
    reader = csv.reader(file)
    itercars = iter(reader)
    next(itercars)
    for row in itercars:
        if row != []:
            search_handle = Entrez.esearch(db="nucleotide",term=row[1], usehistory="y", idtype="acc")   #change row[index]
            search_results = Entrez.read(search_handle)
            search_handle.close()

            acc_list = search_results["IdList"] 
            webenv = search_results["WebEnv"]
            query_key = search_results["QueryKey"]

            fetch_handle = Entrez.efetch(db="nucleotide",rettype="fasta",retmode="text",webenv=webenv,query_key=query_key,idtype="acc")
            data = fetch_handle.read()

            write_file = open(files[no], "w")
            write_file.write(data)

            print("file",no,"done")  # remove
            no+=1

