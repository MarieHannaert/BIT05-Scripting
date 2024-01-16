#!/usr/bin/python3

#Read the gene_species.csv file, available on Leho, line by line
#and print the column names.
import csv
import os
from eutils import Client

eclient = Client(api_key="6ee79cd71573e51c24975440f08fec4d0608")
esearchlist = []
efetchlist = []
genes = []
organisms = []
result_file = open("results.fasta","w")
with open(os.getcwd() + '/' + 'gene_species.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    print("Column names are:")
    result_file = open("results.fasta","w")
    linecount=0
    for row in csv_reader:
        if linecount==0:
            print("{0:5s} | {1:5s}".format(row[0],row[1]))
            linecount +=1
        elif linecount >=1:
            genes.append(row[0]) 
            organisms.append(row[1])
            gene_esearch = eclient.esearch(db='protein', term=row[0]+ '[Gene] AND ' + row[1]  + '[Organism]')
            obj_summary_list = dir(gene_esearch)
            esearchlist.append(gene_esearch.ids[0])
    for ids in esearchlist:
        protein_efetch = eclient.efetch(db='protein', id=ids)
        obj_protein_list = dir(protein_efetch)
        refseq = protein_efetch.gbseqs[0]
        refseq_list = dir(refseq)
        efetchlist.append(refseq.sequence)
for w, x, y, z in zip(genes, organisms, esearchlist, efetchlist):
    result_file.write(">"+str(w)+"_"+str(x)+"_id="+str(y)+"\n")
    result_file.write(str(z) + "\n")
    print(">"+str(w)+"_"+str(x)+"_id="+str(y)+"\n"+str(z))
                    
result_file.close()



#print(genes)
#print(organisms)
#print(esearchlist)
#print(efetchlist)



