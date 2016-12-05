def regularsearch(my_list, pattern):
    import re
    for p in [i for i, x in enumerate(my_list) if re.search(pattern, x)]:
        return a[p]
