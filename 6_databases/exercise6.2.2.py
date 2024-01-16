#!/usr/bin/python3
################################################################################
# MySQL (example-code-6-ensembl.py)
################################################################################
import MySQLdb as my
import sqlite3

# Reading data from Ensembl
print("\nREADING DATA FROM ENSEMBL DATABASE")
# Core databases: <genus_species>_core_<version>_<assembly_version>
# Ensembl Release 104 (May 2021)
db = my.connect(host="ensembldb.ensembl.org", user="anonymous", passwd="",
                db="homo_sapiens_core_104_38")

conn = sqlite3.connect('ensembl.db')
# Next create cursor object
# and call its execute() method to perform SQL query
ensembl_db= conn.cursor()
original_db= db.cursor()


no_rows3 = original_db.execute("""SELECT transcript.stable_id, gene.stable_id, gene.description FROM transcript join gene on gene.gene_id=transcript.gene_id""")
result=original_db.fetchall()
print(result)

try:
    ensembl_db.execute('''CREATE TABLE test \
            (transcript_stable_id, gene_stable_id, description)''')
except sqlite3.OperationalError:
    print("\nTable test already exists\n")

for n in result:
    ensembl_db.execute('''INSERT INTO test \
             VALUES(?,?,?)''', \
            n)
# Save (commit) changes
conn.commit()
# Close connection when done with it
conn.close()