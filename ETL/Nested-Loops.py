#Nested list comprehensions and generator expressions:

[(i,j) for i in range(3) for j in range(i) ]

((i,j) for i in range(4) for j in range(i) )

#These can replace huge chunks of nested-loop code.
