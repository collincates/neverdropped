ca_cities_dict = {
                "Bakersfield": "bakersfield",
                "Chico": "chico",
                "Corcoran": "hanford",
                "Fresno": "fresno",
                "Gold Country": "goldcountry",
                "Hanford": "hanford",
                "Humboldt County": "humboldt",
                "Imperial County": "imperial",
                "Inland Empire": "inlandempire",
                "Lake Tahoe": "reno",
                "Los Angeles": "losangeles",
                "Madera": "fresno",
                "Mendocino County": "mendocino",
                "Merced": "merced",
                "Modesto": "modesto",
                "Monterey Bay": "monterey",
                "Orange County": "orangecounty",
                "Palm Springs": "palmsprings",
                "Redding": "redding",
                "Reno": "reno",
                "Riverside": "inlandempire",
                "Sacramento": "sacramento",
                "San Bernardino": "inlandempire",
                "San Diego": "sandiego",
                "San Francisco": "sfbay",
                "San Luis Obispo": "slo",
                "Santa Barbara": "santabarbara",
                "Santa Maria": "santamaria",
                "Siskiyou": "siskiyou",
                "Stockton": "stockton",
                "Susanville": "susanville",
                "Sutter": "yubasutter",
                "Tulare": "visalia",
                "Ventura": "ventura",
                "Visalia": "visalia",
                "Yuba": "yubasutter",
}

def make_url(city, search_terms):
#city = input("Enter a city name: ")
#search_terms = input("Enter your search terms: ")

#implement city lookup of all city names in CL. How to handle typos? Eventually this will not be an input() scenario.
#   https://geo.craigslist.org/iso/us/ca


    return f"https://{city}.craigslist.org/search/mcy?format=rss&query={'+'.join([term for term in search_terms.lower().split()])}"


# make search terms a parameter of the module. e.g. "scrape("BMW 250 Series")"

# (optional) assign each term to a category (make, model, etc.)

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

if __name__ == "__main__":
    for city_abbrev in ca_cities_dict:
        print(make_url(ca_cities_dict[city_abbrev], "Kawasaki Ninja"))
