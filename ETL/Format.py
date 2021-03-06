#https://pyformat.info/


"Hello {}, my name is {}".format('john', 'mike')
#'Hello john, my name is mike'.

"{1}, {0}".format('world', 'Hello')
#'Hello, world'

"{greeting}, {}".format('world', greeting='Hello')
#'Hello, world'

data = {'first': 'Hodor', 'last': 'Hodor!'}
'{first} {last}'.format(**data)
#'Hodor Hodor!'

'{first} {last}'.format(first='Hodor', last='Hodor!')
#'Hodor Hodor!'

'hello there %(5)s' % {'5': 'you'}
#'hello there you'
