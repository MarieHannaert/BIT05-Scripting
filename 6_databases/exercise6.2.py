#!/usr/bin/python3
import MySQLdb as my
# Reading data from Ensembl
print("\nReading Ensemble transcript data...")
# Core databases: <genus_species>_core_<version>_<assembly_version>
# Ensembl Release 104 (May 2021)
db = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="",
                db="homo_sapiens_core_104_38")
c = db.cursor()
query= "SELECT transcript.transcript_id, transcript.gene_id, transcript.stable_id, gene.description, gene.stable_id \
        FROM transcript\
        LEFT JOIN gene ON transcript.gene_id = gene.gene_id LIMIT 100"

enst_rows=c.execute(query)
print("\nExample records:")
# Iterate over result
result = c.fetchall()
c=1
for row in result: 
    if (c<6):
         print("Ensembl transcript: {}\n\t{}\n\t{}".format(row[13]))
    c = c+1
