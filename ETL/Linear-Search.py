def lsearch(my_list, term):
    for i in range(len(my_list)):
        if my_list[i] == term:
            return i
        return None
    
my_list = [‘element 1’, ‘item two’, ‘element three’, ‘item 4’]
term = ‘item two’

lsearch(my_list,  term)
item two

position = my_list.index(term)
1
