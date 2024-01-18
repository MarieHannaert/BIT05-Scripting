#!/usr/bin/python3
from openpyxl import Workbook

print("===================================================================")
print("This script will look for Pfam hits of interest in the mouse genome")
print("===================================================================")
Pfam_searchterm=input("Enter a Pfam search term (e.g. card, arm)or type 0 to stop: ")
Pfam_search_list=[]
while Pfam_searchterm != "0":
    Pfam_search_list.append(Pfam_searchterm)
    Pfam_searchterm=input("Enter a Pfam search term (e.g. card, arm)or type 0 to stop: ")
    if Pfam_searchterm== "0":
        print("\nYour Pfam search list:\n {}".format(Pfam_search_list))

import MySQLdb as my
# Reading data from UCSC
print("\nLooking in the UCSC Table Browser for your Pfam list")
db = my.connect(host="genome-mysql.soe.ucsc.edu",
#db = my.connect(host="genome-euro-mysql.soe.ucsc.edu",
   user="genomep",
   passwd="password",
   db="mm39")
c = db.cursor()

wb = Workbook() 
ws = wb.active 
ws.title = "Pfam output"
ws.append(["Chrom","start","end", "name", "score", "strand", "gene(name2)"])

for searchterm in Pfam_search_list:
    print("Getting data for {} using query:\n \t SELECT * FROM ucscGenePfam WHERE name LIKE '{}' """.format(searchterm, searchterm))
    no_rows = c.execute("""SELECT * FROM ucscGenePfam WHERE name LIKE '{}' """.format(searchterm))
    result= c.fetchall()
    print("Found {} matches\n".format(no_rows))

    rowcounter= 0
    for row in result:
        rowcounter += 1
        #ws.append([row[1],row[2],row[3],row[4],row[5],row[6]])

        print("""SELECT DISTINCT name2 FROM ncbiRefSeq WHERE chrom='{}' AND cdsStart<={} AND cdsEnd>={}""".format(row[1], row[2],row[3]))
        no_rows2 = c.execute("""SELECT DISTINCT name2 FROM ncbiRefSeq WHERE chrom='{}' AND cdsStart<={} AND cdsEnd>={}""".format(row[1], row[2],row[3]))            
        result2= c.fetchall()
        print("Found {} gene(s) for Pfam {} in region {}:{}-{}".format(no_rows2, searchterm, row[1], row[2],row[3]))
        rowcounter2= 0
        if no_rows2 != 0:
            for row2 in result2:
                rowcounter2 += 1
                print("\tGene:{}".format(row2[0]))
        elif no_rows2 == 0:
            row2="-"
        ws.append([row[1],row[2],row[3],row[4],row[5],row[6],row2[0]])       
wb.save("pfam.xlsx")



