import datetime
from scraper import _make_rss_loop, _make_rss_single_search, parse, scrape
from wordpresspost import new_wp_post
from constants import URLS_CAN, URLS_UK, URLS_USA, ALL_MAKES
from queries import QUERIES
import time
from random import uniform

random_sleep = round(uniform(6, 8), 1)
"""
# get back to this if speed in an issue # search_terms = lambda make, model: [f"{make} {model}" for model in [model for model in models for [(make, models) for make, models in QUERIES.items()]]
for make, models in QUERIES.items():
    for model in models:
        search_terms = f"{make}+{model}"    #what if either make or model are multiple words? This will not add '+' between them in these cases
        make = make
        model = model
        print(f"\nSearching for {search_terms}\n")

        for area_name, area_urls in URLS_UK.items():
            for url in area_urls:
                # time.sleep(random_sleep)
                print(_make_rss_loop(url, search_terms))

        for area_name, area_urls in URLS_CAN.items():
            for url in area_urls:
                # time.sleep(random_sleep)
                print(_make_rss_loop(url, search_terms))

        for area_name, area_urls in URLS_USA.items():
            for url in area_urls:
                # time.sleep(random_sleep)
                print(_make_rss_loop(url, search_terms))
"""



city = input("Enter a city name: ")
search_terms = input("Enter your search terms: ")

rss_url_to_scrape = _make_rss_single_search(city, search_terms)

cl_posts = scrape(rss_url_to_scrape)
for post in cl_posts:
    new_wp_post(post)

# repeat the below at certain time(s) of day
# datetime setting as variable

daily_scrape = Scraper()
daily_scrape.get_RSS()
daily_scrape.get_URLS()
daily_scrape.make_WP_posts()
daily.scrape.die()


# start with UK

# then with USA EAST
# then with CAN EAST

# then with USA CENTRAL
# then with CAN CENTRAL

# then with USA WEST
# then with CAN WEST

# scrape in timezones?



# listings should be able to be clicked to be removed from the list.
#     (What happens to the listing at this point? Does it's status get updated in the DB as a new category like "viewed"?)
