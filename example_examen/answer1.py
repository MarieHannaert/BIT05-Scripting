#!/usr/bin/python3
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title ="output SNP search "
ws.append(["Accession no.","SNP","Chr:start-stop"])
acc_nmb_list= []
print(acc_nmb_list)

print("This script will look for SNPs using RefSeq accession numbers")
print("=============================================================")
acc_nmb=input("Enter accession no. or type 0 to stop: ")
while acc_nmb != "0":
    acc_nmb_list.append(acc_nmb)
    acc_nmb=input("Enter accession no. or type 0 to stop: ")
    if acc_nmb == "0":
        print("Your list:{}".format(acc_nmb_list))

import MySQLdb as my
# Reading data from UCSC
print("\nREADING DATA FROM UCSC DATABASE")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")
c = db.cursor()

for numb in acc_nmb_list:
    print("Getting SNPs for : {}".format(numb))
    print("using query: SELECT * FROM snp151CodingDbSnp WHERE transcript = '{}' """.format(numb))
    no_rows = c.execute("""SELECT * FROM snp151CodingDbSnp WHERE transcript = %s """ ,(numb,))
    # Fetch one row (ENST + ENSG)
    result= c.fetchall()
    print("Total SNPsnfound in {}: {}".format(numb,no_rows))
    rowcounter= 0
    for row in result:
          rowcounter += 1
          ws.append([numb, row[4], row[1] + ":" + str(row[2]) + "-" + str(row[3])])

wb.save("SNPs.xlsx")









