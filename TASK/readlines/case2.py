f = open('text.txt', 'r')

for line in f:
  line = line.strip()
  print(line)

f.close()