import requests
import json

def get_fundamentals(symbol, api_key):
    url = 'https://eodhistoricaldata.com/api/fundamentals/{}?fmt=json&api_token={}'.format(symbol, api_key)
    return requests.get(url).json()