
# coding: utf-8

# In[1]:

import os, sys


# In[3]:

infile = sys.argv[1]
# infile = 'list.txt'


# In[11]:

with open(infile, 'rt', encoding='utf-8') as f:
    for item in f:
        print(item.strip())
        os.mkdir(item.strip())        

