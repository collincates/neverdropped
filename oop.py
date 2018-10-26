import requests
from bs4 import BeautifulSoup
import time

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
    def __init__(self, city_url, search_terms):
        self.city_url = city_url
        self.search_terms = search_terms
        self.rss_feed = f"{self.city_url}/search/mcy?format=rss&query={self.search_terms.lower()}"


class DailyScrape(object):
    def __init__(self):
        self.rss_feeds_to_scrape = set()
        self.parsed_cl_postings = set()

    def get_RSS_feeds(self):
        #MAKE THIS A LOOP OF ALL INSTANCES OF CLRSSFeed
        #APPEND OR ADD TO self.rss_feeds_to_scrape
        #HOW DOES IT KNOW WHAT SCOPE TO CHECK? WHERE ARE THE FEED OBJECTS?

    def get_CL_post_URLS(self):


    def scrape_CL_post_data(self):


    def make_WP_posts(self):


    def die(self):
