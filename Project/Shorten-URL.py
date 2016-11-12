import requests


#URL shortening is crucial given twitter 140 characters restriction
def shorten_url(longUrl):
    url="https://api-ssl.bitly.com/v3/shorten?access_token="+tokenBitly+"&longUrl="+longUrl
    b = requests.get(url)
    resp = b.json()
    shortUrl = resp["data"]["url"]
    return(shortUrl)
