from Bio import Entrez
Entrez.email = "sera.1@iitj.ac.in" # Always tell NCBI who you are
handle = Entrez.egquery(term="Klebsiella pneumoniae")
record = Entrez.read(handle)

#Now we download the list of GenBank identifiers:
count = 10972
handle = Entrez.esearch(db="nucleotide", term="klebsiella pneumonia[orgn] AND (biomol_genomic[PROP] AND ddbj_embl_genbank[filter])", retmax=count)
record = Entrez.read(handle)
gi_list = record["IdList"]

number = 0
acc_dict = {}

#writing to out_india.txt
newline = "\n"
write_file = open("out_india.txt", "w")
write_file.write("{:<10} {:<40} {:<100}".format('Searchno','Accession ID','Description'))
write_file.write(newline)

for ide in gi_list:
    handle = Entrez.efetch(db="nucleotide", id=ide, rettype="gb", retmode="text") # change db
    data = handle.read()

    string3 = 'India'

    if string3 in data:
        x = int(data.index('ACCESSION'))
        acc_number = data[x:x+30]
        description = data[0:x]
        number += 1
        searchno = number
        write_file.write("{:<10} {:<40} {:<100}".format(searchno,acc_number,description))
        write_file.write(newline)
    else:
        number += 1
        print(number)
