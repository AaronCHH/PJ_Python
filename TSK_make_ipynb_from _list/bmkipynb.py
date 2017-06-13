# coding: utf-8

import os, sys
import nbformat
import nbformat as nbf
nb = nbf.v4.new_notebook()

nameList = sys.argv[1]

with open(nameList, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
#         print(line)
        fname = line
        with open(fname.encode("utf8").decode("utf8", "ignore") + '.ipynb', 'w') as f:
            nbf.write(nb, f)