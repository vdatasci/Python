def rls(my_list, pattern):
    import re
    result = re.findall(pattern, ','.join(str(my_list)))
    return result



def rlsindex(my_list, pattern):
    import re
    r = re.findall(pattern, ','.join(str(my_list)))
    for p in r:
        print my_list.index(p)

