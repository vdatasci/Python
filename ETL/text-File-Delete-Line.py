#read the file
with open('file.txt') as fh:
  data = fh.readlines()

# delete a line (modify the data)
deleted_line = data.pop(randrange(len(data)))

#rewrite the file
with open('file.txt', 'w') as fh:
  fh.write(''.join(data))
