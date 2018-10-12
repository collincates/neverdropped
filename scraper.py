import requests
from bs4 import BeautifulSoup
import time

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
#implement city lookup of all city names in CL. How to handle typos? Eventually this will not be an input() scenario.
#   https://geo.craigslist.org/iso/us/ca

def _make_rss(city, search_terms):
    return f"https://{ca_cities_dict[city]}.craigslist.org/search/mcy?format=rss&query={'+'.join([term for term in search_terms.lower().split()])}"


# return RSS feed entries that contain ALL of the search terms, and only ALL terms
def _get_urls_from_rss(rss_feed_url):
    "Returns a list of posting URLs from a CL RSS feed"
    cl_rss = requests.get(rss_feed_url)
    soup = BeautifulSoup(cl_rss.text, 'html.parser')
    urls = [list_item['rdf:resource'] \
                for list_item in soup.find_all('rdf:li')]
    #print('got list of urls')
    if len(urls) == 0:
        print("Nothing comes up in that area for those terms.")
        exit(0)
    elif len(urls) == 1:
        print("\n\nFound one match...\n\n")
    elif len(urls) > 1:
        print(f"\n\nFound {len(urls)} matches...\n\n")

    return urls


def parse(posting_url):
    #listing title, the location, price, the body text, the images at highest resolution, and the link to the original post.
    cl_posting = requests.get(posting_url)
    soup = BeautifulSoup(cl_posting.text, 'html.parser')

    cl_id = soup.find('div', class_='postinginfos') \
                            .find('p', class_='postinginfo') \
                            .getText().lstrip("post id: ")

    title = soup.find(id='titletextonly').text

    try:
        price = soup.find(class_='price').text
    except AttributeError:
        price = "No price given."

    try:
        location = soup.find('small').text.strip(' () ')
    except AttributeError:
        location = "No location given in original post."

    try:
        body_text = soup.find(id='postingbody').text.replace("\n\nQR Code Link to This Post\n\n\n", '') #contents[2::]
    except AttributeError:
        body_text = "No body text in original post."

    when_posted = soup.find('p', id='display-date') \
                            .find('time', class_='date timeago')['datetime']

    images = [a['href'] for a in soup.find_all('a', class_='thumb', href=True)]

    orig_url = posting_url

    return {
    'cl_id': cl_id,
    'title': title,
    'price': price,
    'location': location,
    'body_text': body_text,
    'when_posted': when_posted,
    'original_url': orig_url,
    'images': images,
    }

def scrape(rss_feed_url):
    url_list = _get_urls_from_rss(rss_feed_url)
    data = []
    for url in url_list[0:1]:

        print(parse(url))
        data.append(parse(url))
        time.sleep(5)
    return data


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
        # collect CL RSS feed using search terms
        link = _make_rss(ca_cities_dict[city_abbrev], "Kawasaki Ninja")
        print(link)
        print(type(link))
