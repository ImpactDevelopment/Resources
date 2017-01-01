'''
Python 3.0 library with functions to convert to and from mc uuid and player names
'''

import json, requests

BASE_URL = 'https://api.mojang.com/'
UUID_URL = BASE_URL + 'users/profiles/minecraft/'
NAME_URL = BASE_URL + '/user/profiles/'

# def getJSON(url, params):
#     response = requests.get(url=url, params=params)
#     return json.loads(response.text)

def hasHyphens(uuid):
    pass

def stripUUID(uuid):
    pass

def hyphenUUID(uuid):
    pass

def hasError(json):
    return json.has_key('error')

def toUUID(name):
    # TODO: JSON request to get the uuid
    respone = requests.get(url=UUID_URL + name)
    json = json.loads(response.text)
    
    if (not hasError(json)):
        return hyphenUUID(json['id'])
    
    return

def fromUUIS(uuid):
    pass
