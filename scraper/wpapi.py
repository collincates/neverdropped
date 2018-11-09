import os
import sys
import datetime
from random import uniform
import time
import requests
from bs4 import BeautifulSoup
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import taxonomies, media
from wordpress_xmlrpc.methods.posts import NewPost, GetPost, GetPosts

random_sleep = round(uniform(6, 8), 1)


class WPSession():
    def __init__(self):
        self.url = os.environ.get('WP_URL')
        self.user = os.environ.get('WP_USER')
        self.password = os.environ.get('WP_PASS')
        self.connection = None
        self.tags = []
        self.wp_post_objects = []
        self.connect()
        self.get_all_tags()

    def connect(self):
        self.connection = Client(self.url, self.user, self.password)
        print("Connection established.")

    def get_all_tags(self):
        try:
            self.tags = self.connection.call(taxonomies.GetTerms('post_tag'))
        except:
            print("A connection has not been established.")
            sys.exit(0)

    def make_new_wp_objects_from(self, cl_post_objects, post_status='draft'):
        # check if a cl_id already exists in the WP DB. If so, pass.
        tag_list = [tag.name for tag in self.tags]

        for object in cl_post_objects:

            if object.cl_id in tag_list:
                print('{} already in database'.format(object.cl_id))
                pass
            # if it's a new cl_id, create a blog post for it.
            else:
                # Upload images from CL posting to WP DB
                if len(object.image_links) == 0:
                    html_formatted_links = []
                    attachment_id = None
                    pass
                else:
                    img_links_from_wp_db = []

                    height = "450"
                    width = "600"
                    thumbnailed = False

                    for img in object.image_links:

                        time.sleep(random_sleep)

                        data = {
                        'name': '{}_{:02d}.jpg'.format(object.cl_id, object.image_links.index(img) + 1),
                        'type': 'image/jpeg',
                        # 'date': 'test',
                        'bits': xmlrpc_client.Binary(requests.get(img).content),
                        }

                        response = self.connection.call(media.UploadFile(data))

                        if thumbnailed == False:
                            attachment_id = response['id']
                            thumbnailed = True
                        else:
                            pass

                        img_links_from_wp_db.append(response['url'])

                    html_formatted_links = list(
                        map(lambda link: f"<img src={link}>", img_links_from_wp_db)
                        )

                # Create WordPressPost object for each new CL post,
                # then append each WPP object to self.wp_post_objects

                post = WordPressPost()
                post.id = None
                post.post_status = post_status
                post.date = datetime.datetime.strptime(
                                object.when_posted, '%Y-%m-%dT%H:%M:%S%z'
                )
                post.title = object.title
                post.thumbnail = attachment_id

                post.content = (
                                f"{object.price}\n" \
                                f"{object.location}\n\n" \
                                f"{object.body_text}\n" \
                                f"{' '.join(html_formatted_links)}\n\n"
                                f"Original Post: <a href={object.orig_url}>{object.orig_url}</a>"
                )

                post.terms_names = {
                    'category': [object.make],
                    'post_tag': [
                                item for sublist in [
                                                    [object.cl_id],
                                                    [object.model],
                                                    object.cl_tags_from_author
                                                    ]
                                for item in sublist
                                ],

                }

                post.custom_fields = [
                    {'key': 'original_posting_url', 'value': object.orig_url},
                    {'key': 'make', 'value': object.make},
                    {'key': 'model', 'value': object.model},
                    {'key': 'cl_id', 'value': object.cl_id},
                    {'key': 'name', 'value': object.cl_id},
                    {'key': 'title', 'value': object.title},
                    {'key': 'price', 'value': object.price},
                    {'key': 'location', 'value': object.location},
                    # {'key': 'country', 'value': object.country},
                    # {'key': 'state', 'value': object.state},
                    # {'key': 'county', 'value': object.county},
                    # {'key': 'city', 'value': object.city},
                    {'key': 'cl_tags_from_author', 'value': object.cl_tags_from_author},
                    {'key': 'body_text', 'value': object.body_text},
                    {'key': 'when_posted', 'value': object.when_posted},
                    {'key': 'cl_image_links', 'value': object.image_links},
                    ]

                self.wp_post_objects.append(post)

    def post_new_wp_objects(self):
        for post_object in self.wp_post_objects:
                post_object.id = self.connection.call(NewPost(post_object))


    def ping_posts(self):
        # get pages in batches of 20
        # offset = 0
        # increment = 20
        # while True:
        #     pub_and_draft_posts = self.connection.call(GetPosts({'post_status': ['publish', 'draft'], 'number': increment, 'offset': offset}))
        #         # if len(posts) == 0:
        #                 break  # no more posts returned
        #         for post in pub_and_draft_posts:
        #                 do_something(post)
        #         offset = offset + increment

        pub_and_draft_posts = self.connection.call(GetPosts({'post_status': ['publish', 'draft'], 'number': 1000}))

        for post in reversed(pub_and_draft_posts):
            time.sleep(random_sleep)
            original_posting_url = [meta['value'] for meta in post.custom_fields if meta['key'] == 'original_posting_url'][0]
            ping_post = requests.get(original_posting_url)
            soup_ping = BeautifulSoup(ping_post.text, 'html.parser')
            if soup_ping.find('div', class_='removed'):
                print(soup.find('h2').getText().split('\n')[0])
                self.connection.call(DeletePost(post))
                print(f'Deleted {post.title}. It was at {original_posting_url}.')
            else:
                print(f'{post.title} is still active at {original_posting_url}.')
                pass

if __name__ == "__main__":
    pass
