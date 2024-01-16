#!/usr/bin/python3

import MySQLdb as my
from openpyxl import Workbook
################################################################################
# Initialize Workbook
wb = Workbook() #wb = workbook
# Active worksheet
ws = wb.active #ws = worksheet
ws.append(["Accession_no.", "SNP", "Chr:start-stop"])
inputcheck = False
Refseqlist = []
while inputcheck == False:
       refseqnumber = input("Please enter a Refseq number, or type 0 to stop: ")
       if refseqnumber == "0":
              inputcheck = True
       else:
            Refseqlist.append(refseqnumber)
print("\nREADING DATA FROM UCSC DATABASE")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="hg38")
cursor1 = db.cursor()
for refseqnumber in Refseqlist:
    print("Getting SNPs for: {}".format(refseqnumber))
    query = cursor1.execute("""SELECT * FROM snp151CodingDbSnp WHERE transcript = '{}'""".format(refseqnumber))
    print('using query: SELECT * FROM snp151CodingDbSnp WHERE transcript = {}'.format(refseqnumber))
    result= cursor1.fetchall()
    print(result)
   
    rowcounter= 0
    for row in result:
          rowcounter += 1
          ws.append([refseqnumber, row[4], row[1] + ":" + str(row[2]) + "-" + str(row[3])])
    print("Total SNPs found for {}: {}".format(refseqnumber,rowcounter))
wb.save("SNP.xlsx")
          