### NCBI Data Retrival
Contains python codes that use Entrez library to fetch NCBI data to your local computer.
These codes specifically help in the retrival of the Indian strains of _Klebsiella pneumoniae_.

#### Important files:
1. **netResultsCsv.py :** retrives results from NCBI (query: Klebsiella pneumoniae AND \"whole genome\" AND India AND (\"300000\"[SLEN] : \"800000\"[SLEN])) to a csv file (indianwholegenome_570.csv)
2. **createFasta.py :** to retrieve the individual genome as seperate files (in fasta/txt format) from the queries in csv input (indianwholegenome_570.csv)
3. **combinedFasta.py :** to retrive combined genome files of the same strains (input : indianwholegenome_570.csv, output: kleb_EN5275.fasta, kleb_5338.fasta...)
