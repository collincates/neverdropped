import datetime
# from scraper import _make_rss_single_search, parse, scrape
# from wordpresspost import new_wp_post
import time
from random import uniform
from CL_API import CLFactory
#  from WP_API import WPFactory

random_sleep = round(uniform(6, 8), 1)


"""
city = input("Enter a city name: ")
search_terms = input("Enter your search terms: ")

rss_url_to_scrape = _make_rss_single_search(city, search_terms)

cl_posts = scrape(rss_url_to_scrape)
for post in cl_posts:
    new_wp_post(post)
"""
# repeat the below at certain time(s) of day
# datetime setting as variable


if __name__ == "__main__":

    cl_factory = CLFactory()
    cl_factory.get_rss_feeds()
    cl_factory.get_cl_posts_from_rss_feeds()

# todo
# daily_scrape.make_WP_posts()
# daily.scrape.die()




# scrape in timezones?

# listings should be able to be clicked to be removed from the list.
#     (What happens to the listing at this point? Does it's status get updated in the DB as a new category like "viewed"?)
