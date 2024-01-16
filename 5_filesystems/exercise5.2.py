#!/usr/bin/python3
import re
import os
import humanfriendly
from openpyxl import Workbook
################################################################################
# Initialize Workbook
wb = Workbook() #object where you store you're information
# Active worksheet
ws = wb.active #active the worksheet 
ws.append(["Sample_ID","File_size"])
htseqcount_dir = "/media/sf_SF/BIT05-scripting/5_filesystems-writing-and-reading/htseqcount/"
htseqcount_list = os.listdir(htseqcount_dir)
print(htseqcount_list)

for filename in htseqcount_list:
    gesplitst_filename=filename.split("_")
    match=re.search("SRR",filename)
    if match:
        pathfile=htseqcount_dir+filename
        size_bytes = os.path.getsize(pathfile)
        hsize = humanfriendly.format_size(size_bytes, binary=True)
        print("file size is {}".format(hsize))
        print("the Sample ID ={}".format(gesplitst_filename[1]))
        ws.append([gesplitst_filename[1],hsize])
    print(gesplitst_filename)
wb.save("ex5.2.xlsx")