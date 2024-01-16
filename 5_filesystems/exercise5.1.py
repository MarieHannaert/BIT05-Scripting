    #!/usr/bin/python3
import re
import csv

fileObj = open("129P2_100000lines.vcf", "r")

line_counter = 1 

for line in fileObj.readlines():#why readlines, because it has commentlines in the beginning 
    match = re.search("^#", line)
    if match: 
        print("line {} = {}".format(line_counter,line))
    elif (line_counter):
        split=line.split("\t")
        print(split)
    
    match = re.search("stop_gained|frameshift", "")
    line_counter += 1 
    if match:
        pass
       
    
fileObj.close()