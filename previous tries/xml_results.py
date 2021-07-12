## Uses xml results to gather info of accession Id and description, writes to out.txt

# importing modules
from Bio import Entrez
import xmltodict

# providing email address
Entrez.email = 'sera.1@iitj.ac.in'       

# generate query to Entrez eSearch
eSearch = Entrez.esearch(db="nucleotide",term="Klebsiella pneumoniae[porgn:__txid573]) AND Klebsiella pneumoniae[porgn:__txid573]", usehistory="y", idtype="acc")

# get eSearch result as dict object
res = Entrez.read(eSearch)

# take a peek of what's in the result (ie. WebEnv, Count, etc.)
# for k in res:
#    print (k, "=",  res[k])

paramEutils = {}     
paramEutils['WebEnv'] = res['WebEnv']         #add WebEnv and query_key to eUtils parameters to request esummary using  
paramEutils['query_key'] = res['QueryKey']    #search history (cache results) instead of using IdList 
paramEutils['rettype'] = 'xml'                #get report as xml
paramEutils['retstart'] = 0                   #get result starting at 0, top of IdList
#paramEutils['retmax'] = 5                    #get next 5 results, by default it returns 10,000 results

# generate request to Entrez eSummary
result = Entrez.esummary(db="nucleotide", **paramEutils)
# get xml result
xml = result.read()
# take a peek at xml
# print(xml)

#convert xml to python dict object for convenient parsing
dsdocs = xmltodict.parse(xml)

#dictionary to store the accession numbers and their strains
acc_dict = {}

#adding the values from the xml result to the dictionary
for ds in dsdocs ['eSummaryResult']['DocSum']: 
    description = ds['Item'][1]['#text']
    acc_number = ds['Item'][12]['#text']
    acc_dict[acc_number] = description


#writing to out.txt
newline = "\n"
write_file = open("out.txt", "w")
write_file.write("{:<15} {:<50}".format('Accession ID','Description',))
write_file.write(newline)

for i in acc_dict:
    Accession_ID = i
    Description = acc_dict[i]
    write_file.write("{:<15} {:<50}".format(Accession_ID, Description))
    write_file.write(newline)

#indian strains - from india refbank and genbank
