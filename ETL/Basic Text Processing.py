### Print Text File contents ###
print(open("F:\Temp Files\TempFile.txt","r").read())

###
### Read lines of Text File ###
file=open('filename.txt','rt')
while true:
	line=file.readline()
	#do something
file.close()

###
### Print elements together of two Arrays ###
list1 = ['a', 'b', 'c', 'd']
list2 = ['p', 'q', 'r', 's']

for x, y in zip(list1,list2):
print x, y

###
### String to Array ###
numstr = '1 2 3 4'
result = map(lambda x:int(x) ,numstr.split())
result
#raw_input()

###
### Concat ###
a = ["Code", "mentor", "Python", "Developer"] 
a.insert(0,"You're")
del a[1]
a.remove('Developer')
print " ".join(a)

###
### Convert to single List Array ###
import itertools 

a = [[1, 2], [3, 4], [5, 6]]
list(itertools.chain.from_iterable(a))

###

