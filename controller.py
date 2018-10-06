from scraper import make_rss, parse, runit
from wordpresspost import new_wp_post


city = input("Enter a city name: ")
search_terms = input("Enter your search terms: ")

rss_url_to_scrape = _make_rss(city, search_terms)

cl_posts = scrape(rss_url_to_scrape)
for post in cl_posts:
    new_wp_post(post)

# repeat the below at certain time(s) of day

# listings should be able to be clicked to be removed from the list.
#     (What happens to the listing at this point? Does it's status get updated in the DB as a new category like "viewed"?)
