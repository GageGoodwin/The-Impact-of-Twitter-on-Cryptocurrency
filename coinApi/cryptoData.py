import requests
import validation
from requests import Request, Session
import json
import pprint

# URL STRINGS TO USE: 
# Historical Data : /v1/quotes/{symbol_id}/history?time_start={time_start}&time_end={time_end}&limit={limit}
# For historical data, you need to use atleast {symbol_id} and {time_start} parameters
# Time must be in 2016-01-01T00:00:00 format
# Symbol Id must be in this format: {exchange_id}_SPOT_{asset_id_base}_{asset_id_quote}
# more info at https://docs.coinapi.io/#historical-data-get-3


url = 'https://rest.coinapi.io/v1/quotes/{symbol_id}/history?time_start={time_start}'.format(symbol_id = 'COINBASE_SPOT_BTC_USD',time_start='2016-01-01T00:00:00')

headers = {'X-CoinAPI-Key':validation.api_key}

session = Session()
session.headers.update(headers)

response = session.get(url)
if response.status_code == 200:
    print(response.text)
else:
    print(response)
