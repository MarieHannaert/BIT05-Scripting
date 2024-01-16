#!/usr/bin/python3
import MySQLdb as my
# Reading data from UCSC
print("\nREADING DATA FROM UCSC DATABASE")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu", this is a backup on the exam
   user="genomep",
   passwd="password",
   db="hg19") #this may be somethig to change on the exam vb. hg38

c = db.cursor()


no_rows = c.execute("""SELECT * FROM ensGene""")
print(c.fetchone())
print("Total rows ensGene:{}".format(no_rows))

nieuw_table=c.execute("""SELECT * FROM ncbiRefSeq where name LIKE 'NM_%'""")
print(nieuw_table)

print("\nREADING DATA FROM UCSC DATABASE")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu", this is a backup on the exam
   user="genomep",
   passwd="password",
   db="hg38") #this may be somethig to change on the exam vb. hg38

d = db.cursor()

tweede_table=d.execute("""SELECT * FROM ncbiRefSeq where name LIKE 'NM_%'""")
print(tweede_table)

print("het verschil tussen 19 en 38 is:",tweede_table-nieuw_table )