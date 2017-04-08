#enumerate

#Wrap an iterable with enumerate and it will yield the item along with its index.

#For example:


a = ['a', 'b', 'c', 'd', 'e']
for index, item in enumerate(a): print index, item

#0 a
#1 b
#2 c
#3 d
#4 e

ranked_users = ['jon','bob','jane','alice','chris']
user_details = [{'name':x, 'rank':i} for i,x in enumerate(ranked_users)]
