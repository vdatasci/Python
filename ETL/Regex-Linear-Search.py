def regularsearch(my_list, term):
    import re
    my_list_pos = [i for i, x in enumerate(my_list) if re.search(term, x)]
    for p in my_list_pos:
        return str(my_list[my_list_pos])
