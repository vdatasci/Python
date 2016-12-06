#Enumerate with different starting index

l = ["spam", "ham", "eggs"]

list(enumerate(l))
#[(0, "spam"), (1, "ham"), (2, "eggs")]

list(enumerate(l, 1))
#[(1, "spam"), (2, "ham"), (3, "eggs")]
