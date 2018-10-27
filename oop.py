import requests
from bs4 import BeautifulSoup
import time
from constants import URLS_CAN, URLS_UK, URLS_USA, ALL_MAKES
from queries import QUERIES


class CLPostObject(object):

    def __init__(self, orig_url, make, model):
        self.orig_url = orig_url
        self.make = make
        self.model = model
        self.parse()

    def parse(self):
        """Parse info from CL post and assign as class instance attributes"""
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

        # Location

        # self.country = country
        # self.state = state
        # self.county = county
        # self.city = city
        #
        try:
            self.location = soup.find('small').text.strip(' () ')
        except AttributeError:
            self.location = "No location entered into original post."

        # Make
        # try:
        #     self.make = soup.find
        # except AttributeError:
        #     self.make = "Make unknown."
        #
        # # Model
        # try:
        #     self.model = soup.find
        # except AttributeError:
        #     self.model = "Model unknown."

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
        self.make = make
        self.model = model
        self.rss_url = f"{self.city_url}/search/mcy?format=rss&query={self.make.lower()}+{self.model.lower()}"


class DailyScrape(object):
    def __init__(self):
        self.rss_objects_to_scrape = []
        self.parsed_cl_postings = []

    def get_RSS_feeds(self):
        # todo: locations to search as arguments? UK=True, USA=True, CAN=True ??
        """
        Concatenate CL URLS in module 'constants' with QUERIES RSS urls  .
        Append all CLRSSFeed objects to this instance of DailyScrape().

        This method does not hit the CL server. No sleep is required.

        # get back to this if speed in an issue # search_terms = lambda make, model: [f"{make} {model}" for model in [model for model in models for [(make, models) for make, models in QUERIES.items()]]

        """

        for make, models in QUERIES.items():
            for model in models:
                # if UK == True:
                for area_name, area_urls in URLS_UK.items():
                    for city_url in area_urls:
                        self.rss_objects_to_scrape.append(CLRSSFeed(city_url, make, model))

                # if CAN == True:
                for area_name, area_urls in URLS_CAN.items():
                    for city_url in area_urls:
                        self.rss_objects_to_scrape.append(CLRSSFeed(city_url, make, model))

                # if USA == True:
                for area_name, area_urls in URLS_USA.items():
                    for city_url in area_urls:
                        self.rss_objects_to_scrape.append(CLRSSFeed(city_url, make, model))


    def get_CL_post_URLS(self):
        pass

    def scrape_CL_post_data(self):
        pass

    def make_WP_posts(self):
        pass

    def die(self):
        pass
