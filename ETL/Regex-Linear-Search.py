def regularsearch(my_list, pattern):
    import re
    return re.findall(pattern, ','.join(my_list))
    return [i for i, x in enumerate(my_list) if re.search(pattern, x)]
