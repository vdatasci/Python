def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        return False
    return True
    
