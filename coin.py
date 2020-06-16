import requests
import json

url ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {'start':'1',
              'limit':'1',
              'convert':'USD'
             }

headers = {
 'Accept': 'application/json',
 'X-CMC_PRO_API_KEY': 'fc83ed05-75a0-4906-bf48-a69ad4c9f243',
}

r = requests.get(url, params=parameters, headers = headers)

#dict
response = r.json()
print (response)