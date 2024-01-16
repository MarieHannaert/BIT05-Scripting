#!/usr/bin/python3
import csv
from eutils import Client
eclient = Client(api_key="4bf09a23633aa3087af235a146b6c336a108")
esearchlist=[]
efetchlist=[]
with open('gene_species.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print column names
            print("Column names are:")
            print("{0:5s} | {1:5s}".format(row[0],row[1]))
            line_count += 1
        elif(line_count<=20):
            # print first 5 lines of data
            print("{0:5s} | {1:5s}".format(row[0],row[1]))
            gene_esearch = eclient.esearch(db='Protein', term=row[0]+row[1])
            #gene_esearch = eclient.esearch(db='protein', term=row[0]+ '[Gene] AND ' + row[1]  + '[Organism]')
            print("\n\nResults of gene esearch:\n{}".format(gene_esearch))
            obj_summary_list = dir(gene_esearch)
            esearchlist.append(gene_esearch.ids[0])
            line_count += 1
    for protein_id in esearchlist:
        protein_efetch=eclient.efetch(db='Protein', id=protein_id)
        obj_protein_list = dir(protein_efetch)
        refseq = protein_efetch.gbseqs[0]
        print(refseq)
        refseq_list = dir(refseq)
        efetchlist.append(refseq.sequence)
        print(efetchlist)
        print(refseq_list)