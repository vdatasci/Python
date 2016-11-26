def ckpage(website):
    import requests
    request = requests.get(website)
    if request.status_code == 200:
            print('1')
    else:
            print('0')
