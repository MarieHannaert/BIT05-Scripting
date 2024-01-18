#!/usr/bin/env python
# coding: utf-8

# # Exploring biopython

# ## Reverse complement

# In[1]:


from Bio.Seq import reverse_complement, transcribe, translate
rcseq = reverse_complement("GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCT")
print("\nReverse complement:\n{}".format(rcseq))


# ## Calculating GC-content

# In[2]:


from Bio.SeqUtils import GC
seq = "GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCT"
print("\nSequence:\n{}".format(seq))
print("\nGC content of seq:\n{:0.1f}%".format(GC(seq)))


# ## Running www BLAST search

# In[3]:


from Bio.Blast import NCBIWWW
help(NCBIWWW.qblast)


# In[4]:


import os
os.getcwd()
f = open("cov2_test.fasta", "r")
print(f.read())


# In[5]:


from Bio import SeqIO
record = SeqIO.read("cov2_test.fasta", format="fasta")
result_handle = NCBIWWW.qblast("blastn","nt",record.seq)


# We need to be a bit careful since we can use result_handle.read() to read the BLAST output only once. \
# Calling result_handle.read() again returns an empty string

# In[6]:


# Saving the blast result
with open("my_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()


# ## Parsing BLAST output

# In[7]:


from Bio.Blast import NCBIXML
result_handle = open("my_blast.xml")


# In[8]:


blast_record = NCBIXML.read(result_handle)
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        print("****Alignment****")
        print("sequence:", alignment.title)
        print("e value:", hsp.expect)


# ## GenBank file parsing

# ### First CDS feature in NC_005816.gb
# 87..1109 \
# /locus_tag="YP_RS22210" \
# /product="IS21-like element IS100 family transposase" \
# /protein_id="WP_000255944.1" \
# /translation="MVTF...RGVA"

# In[9]:


from Bio import SeqIO
record = SeqIO.read("NC_005816.gb", "genbank")
for feature in record.features:
    if feature.type == "CDS":
        print("Locus tag = {}".format(feature.qualifiers.get("locus_tag")))
        print("Product = {}\n".format(feature.qualifiers.get("product")))

