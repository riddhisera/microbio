import csv

from Bio import Entrez
Entrez.email = "sera.1@iitj.ac.in" # Always tell NCBI who you are
handle = Entrez.egquery(term="Klebsiella pneumoniae")
record = Entrez.read(handle)

#Now we download the list of GenBank identifiers:
count = 10972
handle = Entrez.esearch(db="nucleotide", term="klebsiella pneumonia[orgn] AND (biomol_genomic[PROP] AND ddbj_embl_genbank[filter] AND (\"300000\"[SLEN] : \"800000\"[SLEN]))", retmax=count)
record = Entrez.read(handle)
gi_list = record["IdList"]

number = 6227
fields = ['Searchno','Accession ID','Description'] 
filename = "indian_strains_try3.csv"
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile, dialect='excel') 
    csvwriter.writerow(fields)

    for ide in gi_list[6227:10971]:
        handle = Entrez.efetch(db="nucleotide", id=ide, rettype="gb", retmode="text") # change db
        data = handle.read()

        string3 = 'India'

        if string3 in data:
            x = int(data.index('ACCESSION'))
            acc_number = data[x:x+30]
            description = data[0:x]
            number += 1
            searchno = number
            row = [str(searchno),acc_number,description]
            print(row)
            csvwriter.writerow(row)
        else:
            number += 1
            print(number)



