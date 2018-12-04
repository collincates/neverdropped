import datetime
import os
from random import uniform
import sys
import time
from bs4 import BeautifulSoup
import requests
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods.taxonomies import DeleteTerm, GetTerms
from wordpress_xmlrpc.methods.media import GetMediaLibrary, UploadFile
from wordpress_xmlrpc.methods.posts import NewPost, GetPost, GetPosts, DeletePost


random_sleep = round(uniform(6, 8), 1)


class WPSession():
    """
    Create a connection with a WordPress database where raw collected data
    will be stored. All CL objects passed to this class will undergo a check
    to ensure that they do not already exist in the database.
    As a side effect, only new CL objects are written to the WordPress database.
    """

    def __init__(self):
        self.url = os.environ.get('WP_URL')
        self.user = os.environ.get('WP_USER')
        self.password = os.environ.get('WP_PASS')
        self.connection = None
        self.tags = []
        self.wp_post_objects = []

        # Connect to database and get all existing tags
        self.connect()
        self.get_all_tags()

    def connect(self):
        """Create a database connection by passing environment variables."""
        self.connection = Client(self.url, self.user, self.password)
        print("Connection established.")

    def get_all_tags(self):
        """Retrieve all currently existing metadata tags from the database."""
        try:
            self.tags = self.connection.call(GetTerms('post_tag'))
        except:
            print("A connection has not been established.")
            sys.exit(0)

    def make_new_wp_objects_from(self, cl_post_objects, post_status='draft'):
        """
        Convert CL objects into WordPress objects and structure object attributes
        to prepare for database insertion.

        Parameters:
            cl_post_objects (list): List of objects which contain data from CL
                as attributes of the object.

        Optional Parameters:
            post_status (str):  Determines what post status the objects will
                inherit when written to WordPress database. Default is 'draft',
                since we want to review all posts prior to publishing.
                Other options: 'private', 'pending', 'publish', 'trash'.
        """

        # Check if a cl_id already exists in the WP DB. If so, pass.
        tag_list = [tag.name for tag in self.tags]

        for object in cl_post_objects:

            if object.cl_id in tag_list:
                print('{} already in database'.format(object.cl_id))
                pass
            # If it's a new cl_id, create a blog post for it.
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

                        response = self.connection.call(UploadFile(data))

                        if thumbnailed == False:
                            attachment_id = response['id']
                            thumbnailed = True
                        else:
                            pass

                        img_links_from_wp_db.append(response['url'])

                    html_formatted_links = list(
                        map(lambda link: f"<img src={link}>", img_links_from_wp_db)
                        )

                # Create WordPressPost object for each new CL post.
                # Then append each WPP object to self.wp_post_objects.

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
        """Post each new WordPress object to the WordPress database."""
        for post_object in self.wp_post_objects:
                post_object.id = self.connection.call(NewPost(post_object))

    def ping_posts(self):
        """
        Visit original CL URL for each post currently in the WordPress database.
        For any expired, sold, or removed CL posts, set that object's post_status='trash'.
        """
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
                print(soup_ping.find('h2').getText().split('\n')[0])
                self.connection.call(DeletePost(post.id))
                print(f'Deleted {post.title}. It was at {original_posting_url}.')

            else:
                print(f'{post.title} is still active at {original_posting_url}.')


    def cleanup(self):
        """
        Check database trash records (post_status='trash').
        Drop trashed tags, media, and posts from WordPress database.
        """

        # Call all trashed posts, active metadata tags, and photos
        trash_posts = self.connection.call(GetPosts({'post_status': ['trash'], 'number': 1000}))
        active_tag_ids = set([term.id for term in [term for term in [post.terms for post in self.connection.call(GetPosts())] for term in term]])
        active_media_library = self.connection.call(GetMediaLibrary({'number': 1000}))

        # Drop old tags from database
        tag_ids_to_drop = []

        for post in reversed(trash_posts):
            # Bypass Active tags, 'Uncategorized' tags, and cl_id tags
            # Append all other tags to list of terms_to_drop
            for term in post.terms:
                if term.id in active_tag_ids:
                    continue
                # Bypass 'Uncategorized' tags with id='1'
                elif term.id == '1':
                    continue
                elif term.name == [meta['value'] for meta in post.custom_fields if meta['key'] == 'cl_id'][0]:
                    continue
                else:
                    tag_ids_to_drop.append(term)

        for tag in set(tag_ids_to_drop):
            self.connection.call(DeleteTerm('post_tag', tag.id))
            print(f'Deleted this tag from database:\t\tID: {tag.id}\tTag: {tag}')


        # Drop old photos from database
        media_to_drop = []

        for photo in active_media_library:
            #  SHOULD THIS BE SET TO COMPARE MEDIA TO ACTIVE POSTS? CASTS WIDER NET.
            if photo.title[:-7] in [term.name for terms in [posting.terms for posting in trash_posts] for term in terms]:
                media_to_drop.append(photo)
                print(f'Staged this photo for deletion:\t{photo}')

        for photo in reversed(media_to_drop):
            self.connection.call(DeletePost(f'{photo.id}'))
            print(f'Deleted this photo from database:\t{photo}')


        # Delete trashed posts from database
        posts_to_drop = []

        for post in trash_posts:
            # Record with id == 1 is a default WP record that must stay put.
            if post.id == '1':
                continue
            else:
                posts_to_drop.append(post)

        for post in posts_to_drop:
            self.connection.call(DeletePost(post.id))
            print(f'Deleted this post from database:\t{post.title}')

        print(f'\nCleanup is done as of:\t\t\t{datetime.datetime.now().strftime("%c")}\n')

if __name__ == "__main__":
    pass
