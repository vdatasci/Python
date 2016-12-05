def regularsearch(my_list, pattern):
    import re
    r = re.findall(pattern, ','.join(my_list))
    for p in r:
        print my_list.index(p)


    # my_list.index(r)
