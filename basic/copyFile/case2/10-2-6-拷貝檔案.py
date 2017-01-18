with open('poem.txt','rt',encoding = 'utf-8') as fin:
  with open('poem2.txt','wt',encoding = 'utf-8') as fout:
    line = fin.readline()
    while line:
      fout.write(line)
      line = fin.readline()
