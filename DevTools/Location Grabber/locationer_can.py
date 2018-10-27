import requests
from bs4 import BeautifulSoup
import time
from states import *
import json

base_url = 'https://geo.craigslist.org/iso/ca'

canada = dict()

request = requests.get(base_url)
soup = BeautifulSoup(request.text, 'html.parser')

for a in soup.find('div', class_='geo-site-list-container').find_all('a'):
    time.sleep(2)
    print(a)
    canada[a.text]= [a['href']]

# print(json.dumps(uk, indent=1, sort_keys=True))
# print(len(uk))


with open('sites_canada.txt', 'w') as file:
    file.write(json.dumps(canada, indent=1, sort_keys=True))
