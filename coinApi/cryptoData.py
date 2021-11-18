import requests
import validation
from requests import Request, Session
import json
import pprint
import csv
import socket

# URL STRINGS TO USE: 
# Historical Data : /v1/quotes/{symbol_id}/history?time_start={time_start}&time_end={time_end}&limit={limit}
# For historical data, you need to use atleast {symbol_id} and {time_start} parameters
# Time must be in 2016-01-01T00:00:00 format
# Symbol Id must be in this format: {exchange_id}_SPOT_{asset_id_base}_{asset_id_quote}
# more info at https://docs.coinapi.io/#historical-data-get-3

def dogecoin():

    socket.getaddrinfo('localhost', 8080)
    #url = 'https://rest.coinapi.io/v1/quotes/{symbol_id}/history?time_start={time_start}&time_end={time_end}&limit={limit}'.format(symbol_id = 'KRAKEN_SPOT_DOGE_USD',time_start='2020-05-01T00:00:01',time_end='2020-06-01T00:00:01', limit=100000)
    url = 'https://rest.coinapi.io/v1/exchangerate/{asset_id_base}/{asset_id_quote}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}'.format(asset_id_base ='DOGE', asset_id_quote = 'USD', period_id = '1DAY', time_start = '2021-04-01T00:00:00', time_end = '2021-07-01T00:00:00')

    headers = {'X-CoinAPI-Key':validation.api_key2}
    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, timeout=10)
    session.close()
    data_text = ''
    if response.status_code == 200:
        #print(response.text)
        data_text = response.text
        print(data_text)
    else:
        print(response)
        return
    response.close()
    data = json.loads(data_text)
    
    # now we will open a file for writing
    data_file = open('dogecoin_history_rates_apr21-jul21-SNL.csv', 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    
    for history in data:
        if count == 0:
    
            # Writing headers of CSV file
            header = history.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(history.values())
    
    data_file.close()

def bitcoin():

    socket.getaddrinfo('localhost', 8080)
    #url = 'https://rest.coinapi.io/v1/quotes/{symbol_id}/history?time_start={time_start}&time_end={time_end}&limit={limit}'.format(symbol_id = 'KRAKEN_SPOT_DOGE_USD',time_start='2020-05-01T00:00:01',time_end='2020-06-01T00:00:01', limit=100000)
    url = 'https://rest.coinapi.io/v1/exchangerate/{asset_id_base}/{asset_id_quote}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}'.format(asset_id_base ='BTC', asset_id_quote = 'USD', period_id = '1DAY', time_start = '2021-04-01T00:00:00', time_end = '2021-07-01T00:00:00')

    headers = {'X-CoinAPI-Key':validation.api_key3}
    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, timeout=10)
    session.close()
    data_text = ''
    if response.status_code == 200:
        #print(response.text)
        data_text = response.text
        print(data_text)
    else:
        print(response)
        return
    response.close()
    data = json.loads(data_text)
    
    # now we will open a file for writing
    data_file = open('bitcoin_history_rates_apr21-jul21.csv', 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    
    for history in data:
        if count == 0:
    
            # Writing headers of CSV file
            header = history.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(history.values())
    
    data_file.close()

def bitcoinAll():

    socket.getaddrinfo('localhost', 8080)
    #url = 'https://rest.coinapi.io/v1/quotes/{symbol_id}/history?time_start={time_start}&time_end={time_end}&limit={limit}'.format(symbol_id = 'KRAKEN_SPOT_DOGE_USD',time_start='2020-05-01T00:00:01',time_end='2020-06-01T00:00:01', limit=100000)
    url = 'https://rest.coinapi.io/v1/exchangerate/{asset_id_base}/{asset_id_quote}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}&limit={limit}'.format(asset_id_base ='BTC', asset_id_quote = 'USD', period_id = '4HRS', time_start = '2016-01-01T00:00:00', time_end = '2021-11-17T00:00:00', limit = 100000)

    headers = {'X-CoinAPI-Key':validation.api_key3}
    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, timeout=100)
    session.close()
    data_text = ''
    if response.status_code == 200:
        #print(response.text)
        data_text = response.text
        print(data_text)
    else:
        print(response)
        return
    response.close()
    data = json.loads(data_text)
    
    # now we will open a file for writing
    data_file = open('bitcoinAll.csv', 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    
    for history in data:
        if count == 0:
    
            # Writing headers of CSV file
            header = history.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(history.values())
    
    data_file.close()
def dogecoinAll():

    socket.getaddrinfo('localhost', 8080)
    #url = 'https://rest.coinapi.io/v1/quotes/{symbol_id}/history?time_start={time_start}&time_end={time_end}&limit={limit}'.format(symbol_id = 'KRAKEN_SPOT_DOGE_USD',time_start='2020-05-01T00:00:01',time_end='2020-06-01T00:00:01', limit=100000)
    url = 'https://rest.coinapi.io/v1/exchangerate/{asset_id_base}/{asset_id_quote}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}&limit={limit}'.format(asset_id_base ='DOGE', asset_id_quote = 'USD', period_id = '4HRS', time_start = '2016-01-01T00:00:00', time_end = '2021-11-17T00:00:00', limit = 100000)

    headers = {'X-CoinAPI-Key':validation.api_key}
    session = Session()
    session.headers.update(headers)
    
    response = session.get(url, timeout=100)
    session.close()
    data_text = ''
    if response.status_code == 200:
        #print(response.text)
        data_text = response.text
        print(data_text)
    else:
        print(response)
        return
    response.close()
    data = json.loads(data_text)
    
    # now we will open a file for writing
    data_file = open('dogecoinAll.csv', 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    
    for history in data:
        if count == 0:
    
            # Writing headers of CSV file
            header = history.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(history.values())
    
    data_file.close()

dogecoinAll()
