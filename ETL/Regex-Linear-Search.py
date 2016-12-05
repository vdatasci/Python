def regularsearch(my_list, pattern):
    import re
    r = re.findall(pattern, ','.join(my_list))
    return my_list.index(r)
