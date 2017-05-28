# coding: utf-8

import os, sys, glob
from glob import glob

mdlist = glob('*.md')
type(mdlist)


for file in mdlist:

    fp = open(file, 'r', encoding='utf-8')
    lines = []
    for line in fp: # 内置的迭代器, 效率很高
        lines.append(line.rstrip())
    fp.close()

    lines.pop(3)
    lines.insert(2, '<!-- toc orderedList:0 depthFrom:1 depthTo:6 -->') # 在第二行插入
    lines.insert(3, '<!-- tocstop -->') # 在第二行插入
    
    s = '\n'.join(lines)

    fp = open(file, 'w', encoding='utf-8')
    fp.write(s)
    fp.close()
