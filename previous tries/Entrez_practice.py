## checks for INDIA presence in Klebsiella pneumoniae genbanks and prints output

from Bio import Entrez

Entrez.email = "sera.1@iitj.ac.in" 

search_handle = Entrez.esearch(db="nucleotide",term="Klebsiella pneumoniae", usehistory="y", idtype="acc")
search_results = Entrez.read(search_handle)
search_handle.close()

acc_list = search_results["IdList"] 

webenv = search_results["WebEnv"]
query_key = search_results["QueryKey"]
count = 20 # only taking till 20 results as the total obtained from this code: int(search_results["Count"]) is 3290457
batch_size = 5

for start in range(0, count, batch_size):
    end = min(count, start + batch_size)
    print("Going to download record %i to %i" % (start + 1, end)) 
    fetch_handle = Entrez.efetch(db="nucleotide",rettype="genbank",retmode="text",
        retstart=start,
        retmax=batch_size,
        webenv=webenv,
        query_key=query_key,
        idtype="acc",
    )
    data = fetch_handle.read()
    string1 = 'India'
    for line in fetch_handle:  
        if string1 in line:
            print(line)
            break   

fetch_handle.close() 

    
