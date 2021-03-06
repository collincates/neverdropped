import logging
import re
import time
from bs4 import BeautifulSoup
import requests
from scraper.constants import RANDOM_SLEEP, URLS_CAN, URLS_UK, URLS_USA
from scraper.query import get_queries


logging.basicConfig(
    filename='../scraper.log',
    filemode='a',
    format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d - %H:%M:%S',
    level=logging.INFO
)

class CLPostObject(object):
    """
    Create object to hold all details from a CL posting as instance attributes.

    """
    def __init__(self, orig_url, make, model):
        self.orig_url = orig_url
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
        self.image_links = None

        self.parse()

    def parse(self):
        """
        Parse info from CL post and assign data
        as PostObject() instance attributes.

        -!- HITS SERVER, NEEDS SLEEP -!-

        """

        time.sleep(RANDOM_SLEEP)

        # Request CL posting HTML.
        cl_posting = requests.get(self.orig_url)
        soup = BeautifulSoup(cl_posting.text, 'html.parser')

        # Set instance attributes for each necessary item.
        self.cl_id = soup.find('div', class_='postinginfos') \
                            .find('p', class_='postinginfo') \
                                .getText().lstrip("post id: ")
        # Original CL ID
        self.__name__ = self.cl_id

        # Title
        self.title = soup.find(id='titletextonly').text

        # Price
        try:
            self.price = soup.find(class_='price').text
        except AttributeError:
            self.price = "No price given."

        # Location as it was input by original posting author
        try:
            if '(google map)' in soup.find('small').text.strip(' () '):
                pass
            else:
                self.location = soup.find('small').text.strip(' () ')
        except AttributeError:
            self.location = "No location entered into original post."

        # Tags that were input by author of original post
        try:
            cl_meta_area = soup.find('div', class_='mapAndAttrs')('span')
            self.cl_tags_from_author = [
                ' '.join(text) for text in [
                [text for text in field.stripped_strings]
                for field in cl_meta_area]
            ]
        except AttributeError:
            self.cl_tags_from_author = "No CL meta fields exist in original post."

        # Body Text
        try:
            self.body_text = soup.find(
                id='postingbody').text.replace(
                    "\n\nQR Code Link to This Post\n\n\n", ''
                )
        except AttributeError:
            self.body_text = "No body text in original post."

        # Posting Date
        self.when_posted = soup.find('p', id='display-date') \
                                .find('time', class_='date timeago')['datetime']

        # Images. Posting either has zero, one, or multiple images.
        if soup.find('figure', class_='iw multiimage'):
            self.image_links = [
                a['href'] for a in
                soup.find_all('a', class_='thumb', href=True)
            ]
        elif soup.find('figure', class_='iw oneimage'):
            self.image_links = [
                soup.find('div', class_='swipe-wrap')
                .find('img')['src']
            ]
        else:
            self.image_links = []


class CLRSSFeed(object):
    """
    Creat object to hold RSS Feed information for a given search location.
    """
    def __init__(self, city_url, make, model):
        self.city_url = city_url
        self.make = make
        self.model = model
        self.rss_url = f"{self.city_url}/search/mcy?format=rss&query={self.make.lower()}+{self.model.lower()}*"
        self.posting_urls = []

class CLFactory(object):
    def __init__(self):
        self.rss_objects_to_scrape = []
        self.new_cl_postings = []

    def make_rss_feeds(self):
        """
        Concatenate CL URLS in module 'constants' with QUERIES RSS urls.
        Append all CLRSSFeed objects to this instance of CLFactory().

        This method does not hit the CL server. No sleep is required.

        # get back to this if speed in an issue
        # search_terms = lambda make, model:
        # [f"{make} {model}" for model in
        # [model for model in models for
        # [(make, models) for make, models in QUERIES.items()]]

        """
        QUERIES = get_queries()
        SEARCH_AREAS = ['USA', 'UK', 'CAN']
        for make, models in QUERIES.items():
            for model in models:

                if 'USA' in SEARCH_AREAS:
                    for area_name, area_urls in URLS_USA.items():
                        for city_url in area_urls:
                            self.rss_objects_to_scrape.append(
                                CLRSSFeed(city_url, make, model)
                            )
                if 'UK' in SEARCH_AREAS:
                    for area_name, area_urls in URLS_UK.items():
                        for city_url in area_urls:
                            self.rss_objects_to_scrape.append(
                                CLRSSFeed(city_url, make, model)
                            )
                if 'CAN' in SEARCH_AREAS:
                    for area_name, area_urls in URLS_CAN.items():
                        for city_url in area_urls:
                            self.rss_objects_to_scrape.append(
                                CLRSSFeed(city_url, make, model)
                            )

    def get_new_cl_posts_from_rss_feeds(self, compare_to=None):
        """
        Append only new CL posting URLs by comparing any new CL ID's
        to those already present in the database.

        Parameters:
            compare_to (list): List of CL IDs that are already in the database.
                Defaults to 'None', and should instead be passed from the tags
                present in your WordPress session. (wp_session.tags)

        -!- HITS SERVER, NEEDS SLEEP -!-

        """

        # Gather all posting URLS from each of our RSS Feeds.
        self.rss_objects_to_scrape = self.rss_objects_to_scrape
        for rss_object in reversed(self.rss_objects_to_scrape):
            time.sleep(RANDOM_SLEEP)
            request_rss = requests.get(rss_object.rss_url)
            soup = BeautifulSoup(request_rss.text, 'html.parser')
            rss_object.posting_urls = [list_item['rdf:resource'] \
                        for list_item in soup.find_all('rdf:li')]

            # Reduce pings to CL by skipping posts that are in the WP DB.
            for url in reversed(rss_object.posting_urls):
                cl_id = re.split("(\d+).html$", url)[1]

                if cl_id in [tag.name for tag in compare_to]:
                    logging.info(f"{cl_id} was already seen.")
                    rss_object.posting_urls.remove(url)

                else:
                    logging.info(f"Parsing {cl_id}.")
                    self.new_cl_postings.append(
                        CLPostObject(url, rss_object.make, rss_object.model)
                    )
                    logging.info(f"Finished parsing {cl_id}.")

            if len(rss_object.posting_urls) == 0:
                logging.info(f"{rss_object.city_url} has no matches for {rss_object.make} {rss_object.model} today.")
                self.rss_objects_to_scrape.remove(rss_object)
            elif len(rss_object.posting_urls) == 1:
                logging.info(f"{rss_object.city_url} has 1 match for {rss_object.make} {rss_object.model} today.")
            else:
                logging.info(f"{rss_object.city_url} has {len(rss_object.posting_urls)} matches for {rss_object.make} {rss_object.model} today.")

if __name__ == "__main__":
    factory = CLFactory()
    factory.make_rss_feeds()
    for rss in factory.rss_objects_to_scrape:
        print(rss.rss_url)
