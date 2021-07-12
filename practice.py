                                        #~~~~~~~~~~~~~~~~~~ ROUGH CODES ~~~~~~~~~~~~~~~~~#

from Bio import Entrez
Entrez.email = "sera.1@iitj.ac.in" # Always tell NCBI who you are
handle = Entrez.egquery(term="Klebsiella pneumoniae")
record = Entrez.read(handle)

#Now we download the list of GenBank identifiers:
count = 10972
handle = Entrez.esearch(db="nucleotide", term="Klebsiella pneumoniae", retmax=count)
record = Entrez.read(handle)
gi_list = record["IdList"]

number = 0

for ide in gi_list:
    handle = Entrez.efetch(db="nucleotide", id=ide, rettype="gb", retmode="text") # change db
    data = handle.read()

    string3 = 'India'

    if string3 in data:
        print(string3)
        x = int(data.index('ACCESSION'))
        print(data[x+11:x+30])
    else:
        number += 1
        print(number)

#from Bio.Align.Applications import MuscleCommandline
###########################

from Bio import SeqIO
from Bio import Entrez

Entrez.email = "sera.1@iitj.ac.in" 

search_handle = Entrez.esearch(db="nucleotide",term="Klebsiella pneumoniae[porgn:__txid573]) AND Klebsiella pneumoniae[porgn:__txid573]", usehistory="y", idtype="acc")
search_results = Entrez.read(search_handle)
search_handle.close()

acc_list = search_results["IdList"] 
webenv = search_results["WebEnv"]
query_key = search_results["QueryKey"]
count = 20  
batch_size = 1

files = []
k = 0
while k < count:
    # dynamically create key
    files.append("kleb"+str(k)+".fasta")
    k+=1

for file,start in zip(files,range(0, count, batch_size)):
    out_handle = open(file, "w")
    end = min(count, start + batch_size)
    print("Going to download record %i to %i" % (start + 1, end)) 
    fetch_handle = Entrez.efetch(db="nucleotide",rettype="fasta",retmode="text",
        retstart=start,
        retmax=batch_size,
        webenv=webenv,
        query_key=query_key,
        idtype="acc",
    )
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
    out_handle.close()    



