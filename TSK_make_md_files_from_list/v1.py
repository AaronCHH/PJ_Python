
# coding: utf-8

# In[2]:

import os, sys


# In[3]:

infile = sys.argv[1]
# infile = 'list.txt'


# In[19]:

with open(infile, 'rt', encoding='utf-8') as f:
    for item in f:
        print(item.strip())
        fnew = open(item.strip() + '.md', 'a')
        fnew.close()

