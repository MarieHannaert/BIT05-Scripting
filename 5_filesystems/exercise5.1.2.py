#!/usr/bin/python3
import csv

with open("/media/sf_SF/BIT05-scripting/5_filesystems/129P2_OlaHsd.mgp.v5.indels.dbSNP142.normed.vcf") as vcffile:
    with open('test5.1.csv', mode='w') as testfile:
        for n in csv.reader(vcffile, delimiter="\t"):
            if n[0].startswith("#"):
            #    print(''.join(n))
                continue
            #print(n[7])
            if n[7].startswith("INDEL"):
                #print(n[7])
                if "stop_gained" in n[7] or "frameshift" in n[7]:
                    print(n[7])
                    test_writer = csv.writer(testfile, delimiter="|")
                    test_writer.writerow(n[7])
    testfile.close()
                
                
                
        