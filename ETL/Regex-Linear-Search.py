def regularsearch(my_list, pattern):
    import re
    re.findall(pattern, ','.join(my_list))
    #[i for i, x in enumerate(a) if re.search('\w+', x)]
