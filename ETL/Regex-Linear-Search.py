def regularsearch(my_list, term):
    my_list_pos = [i for i, x in enumerate(my_list) if re.search(term, x)]
    result = str(my_list[my_list_pos])
    regularsearch = result
