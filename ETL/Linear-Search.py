def locate(lst, seek):
    for i in range(len(lst)):
        if lst[i] == seek:
            return i
    return None
