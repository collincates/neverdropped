import datetime
from CL_API import CLFactory
# from WP_API import WPFactory

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
# wp_factory.make_WP_posts()
# cl_factory.die()
# wp_factory.die()



# scrape in timezones?

# listings should be able to be clicked to be removed from the list.
#     (What happens to the listing at this point? Does it's status get updated in the DB as a new category like "viewed"?)
