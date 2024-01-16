#!/usr/bin/python3
import sqlite3
import MySQLdb as my
# Reading data from UCSC
print("\nREADING DATA FROM UCSC DATABASE")
db_oud = my.connect(host="genome-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg19") #this may be somethig to change on the exam vb. hg38
c = db_oud.cursor()
no_rows = c.execute("""SELECT * FROM ncbiRefSeq WHERE name LIKE 'NM_%'
""") #this ensGENE may also be something to change on the exam
# Fetch one row (ENST + ENSG)
print(c.fetchone())
print("Total rows ensGene: {}".format(no_rows))

db_nieuw = my.connect(host="genome-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38") #this may be somethig to change on the exam vb. hg38
c = db_nieuw.cursor()
no_rows = c.execute("""SELECT * FROM ncbiRefSeq WHERE name LIKE 'NM_%'
""") #this ensGENE may also be something to change on the exam
# Fetch one row (ENST + ENSG)
print(c.fetchone())
print("Total rows ensGene: {}".format(no_rows))