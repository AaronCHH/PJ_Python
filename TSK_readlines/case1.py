f = open('text.txt', 'r')

for line in f.readlines():
  line = line.strip()
  print(line)


f.close()  