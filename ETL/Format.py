"Hello {}, my name is {}".format('john', 'mike')
#'Hello john, my name is mike'.

"{1}, {0}".format('world', 'Hello')
#'Hello, world'

"{greeting}, {}".format('world', greeting='Hello')
#'Hello, world'

data = {'first': 'Hodor', 'last': 'Hodor!'}
'{first} {last}'.format(**data)
#'Hodor Hodor!'
