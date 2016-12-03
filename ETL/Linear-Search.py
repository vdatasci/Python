def lsearch(my_list, term):
    for i in range(len(my_list)):
        if my_list[i] == term:
            return i
        return None
