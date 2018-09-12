
city = input("Enter a city name: ")
search_terms = input("Enter your search terms: ")

#implement city lookup, with typos accounted for? maybe just a dict of all city names in CL)
cities_dict = {"San Francisco": "sfbay",
                "San Diego": "sandiego",
                "Los Angeles": "losangeles",
}


full_URL = f"https://{cities_dict[city]}.craigslist.org/search/mcy?format=rss&query=\
{'+'.join([term for term in search_terms.lower().split()])}"

print(full_URL)
# get search terms, make this a parameter of the module. e.g. "scrape("BMW 250 Series")"
# split search terms on whitespace, (optional) assign each term to a category (make, model, etc.)
#
# collect CL RSS feed using search terms
# store feed into memory
#
# return RSS feed entries that contain ALL of the search terms, and only ALL terms
#
# check feed repetition by comparing URLs, maybe something else is a better identifier
#
# any new items are added to the main DB set
# any repeated items are sent to a discarded set
# any items that do not appear in the RSS feed and haven't been sent to the main DB
#     or discarded set are added to the expired/closed/sold set
#
#
# update DB with the above "statuses" on each listing
# OR
# update dict that organizes each listing into {current: x, expired/closed/sold: y, discarded/reposts: z}
# save into CSV file, or JSON array, or other DB
#
# scraper module returns set() of listings in the {current: x} category
#     (other categories are still added to the DB file, etc. as above)
