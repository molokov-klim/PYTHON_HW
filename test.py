import requests

def test():

    res = requests.get('http://api.randomuser.me/?results=5')

    print(res.text)




