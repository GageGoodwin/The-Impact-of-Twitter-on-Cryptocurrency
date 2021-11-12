import validation
from requests import Request, Session
import json
import pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'

parameters = {
    'slug':'bitcoin',
    'convert':'USD'
}

headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':validation.api_key
}


session = Session()
session.headers.update(headers)

response = session.get(url,params=parameters)
data = json.loads(response.text)
pprint.pprint(data['data']['1']['quote']['USD']['price'])