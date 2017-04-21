from random import choice
possible_destinations = ["Berlin", "Hamburg", "Munich", 
                         "Amsterdam", "London", "Paris", 
                         "Zurich", "Heidelberg", "Strasbourg", 
                         "Augsburg", "Milan", "Rome"]
print(choice(possible_destinations))


from numpy.random import choice
print(choice(possible_destinations))


x1 = choice(possible_destinations, size=3)
print(x1)
x2 = choice(possible_destinations, size=(3, 4))
print(x2)


print(choice(possible_destinations, size=(3, 4), replace=False))
