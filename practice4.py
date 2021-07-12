from Bio import Entrez

Entrez.email = "sera.1@iitj.ac.in" 

search_handle = Entrez.esearch(db="nucleotide",term="NZ_VINI01000137", usehistory="y", idtype="acc")
search_results = Entrez.read(search_handle)
search_handle.close()
acc_list = search_results["IdList"] 
webenv = search_results["WebEnv"]
query_key = search_results["QueryKey"]

for ide in acc_list:
    print(ide)
    fetch_handle = Entrez.efetch(db="nucleotide",rettype="fasta",retmode="text",webenv=webenv,query_key=query_key,id=ide,idtype="acc",)
    data = fetch_handle.read()
    print(data)