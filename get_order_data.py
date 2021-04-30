import bigcommerce
import requests
import json
from pprint import pprint
from requests_oauthlib import OAuth1

from bcapidetails import ACCESS_TOKEN, CLIENT_SECRET, CLIENT_ID, API_PATH, STORE_HASH

order = 643259
query_url = API_PATH + "orders/" + str(order) + "/products"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'x-auth-token': ACCESS_TOKEN
}

response = requests.request("GET", query_url, headers=headers)

data = response.json()
# pprint(type(data))
for items in data:
    items['product_options'] = dict(items['product_options'][0])
# pprint(type(data[0]['product_options']))
pprint(data)
with open('order.txt', 'w') as outfile:
    json.dump(data, outfile)
