#!/usr/bin/python3
import Bio

#standard output here is an object look at the cookbook to convert to a string 
from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print(my_seq)
print(my_seq.complement())
print(my_seq.reverse_complement())
print(my_seq.reverse_complement_rna())

from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print("gc_fraction:", gc_fraction(my_seq))

from Bio.Seq import Seq
list_of_seqs = [Seq("ACGT"), Seq("AACC"), Seq("GGTT")]
concatenated = Seq("")
for s in list_of_seqs:
    concatenated += s
print(concatenated)

from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_id[1]
mito_table = CodonTable.unambiguous_dna_by_id[2]
#You can compare the actual tables visually by printing them:
print(standard_table)

from Bio import SeqIO
identifiers = [seq_record.id for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank")]
print(identifiers)

from Bio.Blast import NCBIWWW

import os
os.getcwd()
f = open("cov2_test.fasta", "r")
print(f.read())
from Bio import SeqIO
record = SeqIO.read("cov2_test.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastn","nt",record.seq)
# Saving the blast result
with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()

from Bio.Blast import NCBIXML
result_handle = open("my_blast.xml")
blast_record = NCBIXML.read(result_handle)
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        print("****Alignment****")
        print("sequence:", alignment.title)
        print("e value:", hsp.expect)

from Bio import SeqIO
record = SeqIO.read("NC_005816.gb", "genbank")
for feature in record.features:
    if feature.type == "CDS":
        print("Locus tag = {}".format(feature.qualifiers.get("locus_tag")))
        print("Product = {}\n".format(feature.qualifiers.get("pqroduct")))
