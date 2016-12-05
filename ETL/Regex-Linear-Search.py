def regularsearch(my_list, pattern):
    import re
    r = re.findall(pattern, ','.join(my_list))
    for p in r:
        print p



    # my_list.index(r)
