#!/usr/bin/env python
# coding: utf-8

# # Pandas

# In[1]:


# Import module
import pandas as pd


# In[2]:


# Read csv 
df = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/boot/urine.csv")
# Pandas can also read other data formats
# pd.read_excel('file.xlsx',sheet_name='Sheet1', index_col=None, na_values=['NA'])


# In[4]:


# List first 5 rows
df.head(5)


# In[5]:


print("Dimensions of data frame: {}".format(df.shape))
print("Column names: {}".format(df.columns))


# In[6]:


# Check data type of particular column
print("Data type of r column: {}".format(df['r'].dtype))
print("Data type of gravity column: {}".format(df['gravity'].dtype))


# In[7]:


# Data type of all columns
print("Data type of all columns:\n{}".format(df.dtypes))


# In[7]:


# Basic statistics
print("\nMIN: ", df.min())
print("\nMAX: ", df[['calc']].max())
print("\nMEAN: ", df[['calc']].mean())
print("\nMEDIAN: ", df[['osmo']].median())
print("\nSTD: ", df[['osmo']].std())
# Descriptive stats for numeric columns
print("\nDESCRIBE: ", df[['ph']].describe())


# In[8]:


# Drop rows with missing values
df_no_na = df.dropna()
print(df_no_na.head(5))


# In[9]:


# Group data using r
df_r = df.groupby(['r'])
# Calculate mean calc for groups
print("Means for r groups: {}".format(df_r.mean()))


# In[10]:


# Filter/subset data
df_sub = df[ df['calc']>9 ]
print("\nSubset calc>9:\n", df_sub)
print("\nSubset calc column only:\n", df_sub['calc'])


# In[11]:


# Select rows where r=1
df_r1 = df[ df['r']==1 ]
print("\nRows where r=1:\n", df_r1)
# Select and filter
df_r1_calc4 = df[ (df['r']==1) & (df['calc']<4) ]
print("\nRows where r=1 and calc<4:\n", df_r1_calc4)


# In[12]:


# Selecting/slicing rows (first row position 0!)
print("Rows 41-50: ", df[40:50])


# In[13]:


# Select rows and columns with loc method
df_loc = df.loc[40:50,['r','calc']]
print(df_loc)


# In[14]:


# Select rows and columns using positions with iloc method
df_iloc = df.iloc[40:50,[1,3,7]]
print("\nMethod iloc:\n", df_iloc)
# One column by position in df_r1_calc4 subset
print("\nColumn selection by position\n", df_r1_calc4[df_r1_calc4.columns[3]])
print("\nColumn selection 2 by position\n", df_r1_calc4.iloc[:,3])
# Another example with iloc method
df_iloc2 = df.iloc[[0,44,45,78], [1,3]]
print("\nAnother example of iloc:\n", df_iloc2)


# In[15]:


# Sorted by column calc
df_sorted = df.sort_values( by='calc', ascending=False)
# df_sorted
# shift+tab for doc
# Last rows with tail()
df_sorted.tail()


# # NumPY

# ### NDARRAY OBJECT

# In[16]:


# Import module
import numpy as np

# Create numpy array
a = np.array([1,2,3]) 
print("\n1D array:\n",a)

# With more than one dimension 
b = np.array([[1, 2], [3, 4]]) 
print("\n2D array:\n",b)

# Set minimum dimensions
c = np.array([1,2,3], ndmin = 2) 
print("\nMin.dim.:\n",c)


# ### NDARRAY SCALAR DATA TYPES (dtype)
# 
# Different scalar data types defined in NumPy.
# 
# NumPy numerical types are instances of dtype (data-type) object.
# 
# The dtype object describes interpretation of fixed block of memory.

# In[17]:


# np.int8: -128 to 127
x = np.int8([1,2,4])
print("x (int8): {} --> type: {}".format(x,type(x)))

# np.float32
y = np.float32(1.0)
print("y (float32): ", y)

# np_uint8 (unsigned long)
z = np.arange(3, dtype=np.uint8)
print("z (uint8): ", z)

# Convert type using astype() method
zf = z.astype(float) 
print("uint8 to float: ", zf)

# To know/show dtype
print("Type of z = {}\nType of zf = {}".format(z.dtype,zf.dtype))


# In[18]:


# EXAMPLE 1: population data
dt = np.dtype([('country', 'U20'), 
               ('density', 'i4'), 
               ('area', 'i4'), 
               ('population', 'i4')])
# To use 32-bit signed integer: np.dtype('i4')
# To use 64-bit floating-point number: np.dtype('f8')
# To use actual strings in Python 3 use U or np.unicode
# e.g. 25-character string: np.dtype('U20')

# Create nparray with population data
np_population = np.array([
    ('Netherlands', 393, 41526, 16928800),
    ('Belgium', 337, 30510, 11007020),
    ('United Kingdom', 256, 243610, 62262000),
    ('Germany', 233, 357021, 81799600),
    ('Liechtenstein', 205, 160, 32842),
    ('Italy', 192, 301230, 59715625),
    ('Switzerland', 177, 41290, 7301994),
    ('Luxembourg', 173, 2586, 512000),
    ('France', 111, 547030, 63601002),
    ('Austria', 97, 83858, 8169929),
    ('Greece', 81, 131940, 11606813),
    ('Ireland', 65, 70280, 4581269),
    ('Sweden', 20, 449964, 9515744),
    ('Finland', 16, 338424, 5410233),
    ('Norway', 13, 385252, 5033675)],
    dtype=dt)


# In[19]:


# Show first 4 elements
print(np_population[:4])

# Iterate over ndarray with for loop
for element in np_population:
    print("\nCountry: {} has population of {}".format(element[0],element[3]))


# ### NDARRAY ATTRIBUTES
# 
# Array attributes reflect information about the array itself.
# 
# Using its attributes you can get (and sometimes set) properties of array without creating a new array.

# In[20]:


# dtype
print("DTYPE:\n", np_population.dtype)

# Information about the memory layout of the array 
print("FLAGS:\n", np_population.flags)


# In[21]:


# Number of array dimension
print("NDIM:\n", np_population.ndim)

# Tuple of array dimensions
print("SHAPE:\n", np_population.shape)

# Number of elements in array
print("SIZE:\n", np_population.size)

# Length of one array element in bytes
print("ITEMSIZE:\n", np_population.itemsize)

# Total bytes consumed by the elements of the array
print("NBYTES:\n", np_population.nbytes)


# ### NDARRAY METHODS

# In[22]:


# Copy element of array to standard Python scalar and return it
population_element = np_population[1]
print("Second element from population ndarray:\n", population_element)
    
# Return array as a (possibly nested) list
population_list = np_population.tolist()
print("List:\n", population_list)

# Insert scalar into array, last argument is item
np_population.itemset(1, ('BELGIUM', 337, 30510, 11007020) )
print("ndarray.itemset:\n", np_population[1])


# ### BIOPYTHON

# In[23]:


#Import SeqIO from biopython 
from Bio import SeqIO


# In[24]:


# Example 2: storing nucleotide frequencies in nparray
def freq_numpy(dna_list):
    frequency_matrix = np.zeros((4, len(dna_list[0])), dtype=np.int32)
    base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base2index[base]][index] += 1
    return frequency_matrix

mm10_dna = "ACACTCAACTGTTTTAGAAG"
print("Frequences of mm10_dna:\n", freq_numpy(mm10_dna))


# In[25]:


# Import SeqIO from biopython
from Bio import SeqIO
# Fasta file from Leho in jupyter notebook folder
fasta_file = open("mm10_dna.fasta","r")
for seq_record in SeqIO.parse(fasta_file, "fasta"):
    # Get length of fasta record
    print("\nLength of mm10_dna.fasta: ", len(seq_record))
    # Calculate frequencies
    print("\nFrequencies:\n", freq_numpy(seq_record))
fasta_file.close()

