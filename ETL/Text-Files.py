#counting lines in a text file:
with open('file.txt') as f:
    line_count = sum(1 for _ in f)
    print(line_count)

#Selecting random line in text file:
with open('file.txt') as fh:
  line_fetched = random.choice(fh.readlines())
fh.close()  
