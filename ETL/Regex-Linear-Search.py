def regularsearch(my_list, term):
        import re
        for i in range(len(my_list)):
                if my_list[i] == re.compile(term):
                    return i
                return None
