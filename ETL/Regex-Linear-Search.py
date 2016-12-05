def regularsearch(my_list, pattern):
    import re
    r = re.findall(pattern, ','.join(my_list))
    return r
    # my_list.index(r)
