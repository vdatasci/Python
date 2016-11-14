import requests

tokenBitly = '9b66f572ea565ad186c0a78836113264fa8d051a'

def shorten_url(longUrl):
    url="https://api-ssl.bitly.com/v3/shorten?access_token="+tokenBitly+"&longUrl="+longUrl
    b = requests.get(url)
    resp = b.json()
    shortUrl = resp["data"]["url"]
    return(shortUrl)
