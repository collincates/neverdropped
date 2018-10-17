import requests
from bs4 import BeautifulSoup
import time
from states import *
import json

base_url = 'https://geo.craigslist.org/iso/us/'

united_states = dict()

for state, abbv in us_states.items():
    time.sleep(3)
    full_url = str(base_url + abbv)
    request = requests.get(full_url)
    soup = BeautifulSoup(request.text, 'html.parser')
    try:
        county_urls = [i['href'] for i in soup.find('div', class_='geo-site-list-container').find_all('a')]
    except AttributeError:
        if abbv == 'DE':
            county_urls = 'https://delaware.craigslist.org/'
        if abbv == 'HI':
            county_urls = 'https://honolulu.craigslist.org/'
        if abbv == 'ME':
            county_urls = 'https://honolulu.craigslist.org/'
        if abbv == 'NH':
        if abbv == 'RI':
        if abbv == 'VT':
        if abbv == 'WY':

    united_states[abbv] = county_urls

# print(json.dumps(united_states, indent=1, sort_keys=True))

with open('saved.txt', 'w') as file:
    file.write(json.dumps(united_states, indent=1, sort_keys=True))
