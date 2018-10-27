from random import uniform
import time
from bs4 import BeautifulSoup
import requests
from constants import URLS_CAN, URLS_UK, URLS_USA, ALL_MAKES
from queries import QUERIES


random_sleep = round(uniform(6, 8), 1)

seen_listings = set()

class CLPostObject(object):

    def __init__(self, orig_url, make, model): # ,country, state, county, city):
        self.orig_url = orig_url

        # self.country_name = country    implement to pass along for tags
        # self.state_name = state        implement to pass along for tags
        # self.county_name = county      implement to pass along for tags
        # self.city_name = city          implement to pass along for tags

        self.make = make
        self.model = model

        self.cl_id = None
        self.__name__ = None
        self.title = None
        self.price = None
        self.location = None
        self.cl_tags_from_author = None
        self.body_text = None
        self.when_posted = None
        self.images = None

        self.parse()

    def parse(self):
        """
        Parse info from CL post and assign data as class instance attributes

        -!- HITS SERVER, NEEDS SLEEP -!-

        """

        time.sleep(random_sleep)

        cl_posting = requests.get(self.orig_url)
        soup = BeautifulSoup(cl_posting.text, 'html.parser')


        self.cl_id = soup.find('div', class_='postinginfos') \
                            .find('p', class_='postinginfo') \
                                .getText().lstrip("post id: ")

        self.__name__ = self.cl_id

        self.title = soup.find(id='titletextonly').text

        # Price
        try:
            self.price = soup.find(class_='price').text
        except AttributeError:
            self.price = "No price given."

        # Location input by original posting author
        try:
            self.location = soup.find('small').text.strip(' () ')
        except AttributeError:
            self.location = "No location entered into original post."

        # Tags that were input by author of original post
        try:
            cl_meta_area = soup.find('div', class_='mapAndAttrs')('span')
            self.cl_tags_from_author = [' '.join(text) for text in [[text for text in field.stripped_strings] for field in cl_meta_area]]
        except AttributeError:
            self.cl_tags_from_author = "No CL meta fields were entered by post author into original post."

        # Body Text
        try:
            self.body_text = soup.find(id='postingbody').text.replace("\n\nQR Code Link to This Post\n\n\n", '') #contents[2::]
        except AttributeError:
            self.body_text = "No body text in original post."

        # Posting Date
        self.when_posted = soup.find('p', id='display-date') \
                                .find('time', class_='date timeago')['datetime']

        # Images
        self.images = [a['href'] for a in soup.find_all('a', class_='thumb', href=True)]


class CLRSSFeed(object):
    def __init__(self, city_url, make, model):
        self.city_url = city_url
        # self.country_name = country    implement to pass along for tags
        # self.state_name = state        implement to pass along for tags
        # self.county_name = county      implement to pass along for tags
        # self.city_name = city          implement to pass along for tags
        self.make = make
        self.model = model
        self.rss_url = f"{self.city_url}/search/mcy?format=rss&query={self.make.lower()}+{self.model.lower()}"


class CLFactory(object):
    def __init__(self):
        self.rss_objects_to_scrape = []
        self.parsed_cl_postings = []

    def get_rss_feeds(self):
        # todo: locations to search as arguments? UK=True, USA=True, CAN=True ??
        """
        Concatenate CL URLS in module 'constants' with QUERIES RSS urls.
        Append all CLRSSFeed objects to this instance of CLFactory().

        This method does not hit the CL server. No sleep is required.

        # get back to this if speed in an issue # search_terms = lambda make, model: [f"{make} {model}" for model in [model for model in models for [(make, models) for make, models in QUERIES.items()]]

        """

        for make, models in QUERIES.items():
            for model in models:

                # if USA == True:
                for area_name, area_urls in URLS_USA.items():
                    for city_url in area_urls:
                        self.rss_objects_to_scrape.append(CLRSSFeed(city_url, make, model))

                # if UK == True:
                for area_name, area_urls in URLS_UK.items():
                    for city_url in area_urls:
                        self.rss_objects_to_scrape.append(CLRSSFeed(city_url, make, model))

                # if CAN == True:
                for area_name, area_urls in URLS_CAN.items():
                    for city_url in area_urls:
                        self.rss_objects_to_scrape.append(CLRSSFeed(city_url, make, model))


    def get_cl_posts_from_rss_feeds(self):
        """
        Appends all applicable CL posting URLs from a CL RSS feed object

        -!- HITS SERVER, NEEDS SLEEP -!-

        """

        for rss_object in self.rss_objects_to_scrape:
            time.sleep(random_sleep)
            request_rss = requests.get(rss_object.rss_url)
            soup = BeautifulSoup(request_rss.text, 'html.parser')
            urls = [list_item['rdf:resource'] \
                        for list_item in soup.find_all('rdf:li')]
            if len(urls) == 0:
                print(f"{rss_object.city_url} has no matches for {rss_object.make} {rss_object.model} today.")

            else:
                for url in urls:
                    # This will reduce pings to the CL server by skipping over
                    # anything that's already in the WP DB.
                    cl_id = re.split("(\d+).html$", url)[1]

                    if cl_id in seen_listings:
                        print(f"{cl_id} was already seen.")
                        pass

                    else:
                        print('parsing and appending')
                        self.parsed_cl_postings.append(CLPostObject(url, rss_object.make, rss_object.model))
                        print('finished parsing and appending')


    def die(self):
        pass
