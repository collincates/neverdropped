import datetime
from random import uniform
import time
import requests
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import taxonomies, media
from wordpress_xmlrpc.methods.posts import NewPost, GetPost
# import base64

# from wordpress_xmlrpc.methods.users import GetUserInfo

random_sleep = round(uniform(6, 8), 1)


# class WPPostObject():
#     def __init__(self, cl_post_object, post_status='draft'):
#         self.id = None
#         self.post_status = post_status
#         self.orig_url = cl_post_object.orig_url
#         self.make = cl_post_object.make
#         self.model = cl_post_object.model
#         self.cl_id = cl_post_object.cl_id
#         self.__name__ = cl_post_object.__name__
#         self.title = cl_post_object.title
#         self.price = cl_post_object.price
#         self.location = cl_post_object.location
#         self.cl_tags_from_author = cl_post_object.cl_tags_from_author
#         self.body_text = cl_post_object.body_text
#         self.when_posted = cl_post_object.when_posted
#         self.image_links = cl_post_object.image_links
#         self.attachment_id = None
#
#     def upload_images(self):
#         """
#         Read data from CL image URLs, upload a copy of images to WP DB
#         in order to avoid directly linking to CL postings.
#
#         -!- HITS SERVER, NEEDS SLEEP -!-
#
#         """
#
#         img_links_from_wp_db = []
#
#         height = "450"
#         width = "600"
#         thumbnailed = False
#
#         for img in self.image_links:
#
#             # time.sleep(5)
#             # image = WordPressMedia()
#             # image._def['title'] = '{}_{:02d}.jpg'.format(cl_post_object['cl_id'], cl_post_object['images'].index(img))
#             # image._def['parent'] = int(post_ident)
#             # response = self.connection.call(media.UploadFile(image))
#             # print(response._def['link'])
#
#             time.sleep(random_sleep)
#
#             data = {
#             'name': '{}_{:02d}.jpg'.format(self.cl_id, self.image_links.index(img) + 1),
#             'type': 'image/jpeg',
#             'bits': xmlrpc_client.Binary(requests.get(img).content),
#             }
#             # data['bits'] = xmlrpc_client.Binary(requests.get(img).content)
#
#             response = self.connection.call(media.UploadFile(data))
#
#             if thumbnailed == False:
#                 self.attachment_id = response['id']
#                 thumbnailed = True
#             else:
#                 pass
#
#             img_links_from_wp_db.append(response['url'])
#
#         html_formatted_links = list(
#             map(lambda link: f"<img src={link}>", wp_db_img_links)
#             ) # height={height} width={width}>", wp_db_img_links))
#
#         print(html_formatted_links)



class WPSession():
    def __init__(self):
        self.url = 'http://localhost:8888/motocl/xmlrpc.php'
        self.user = 'collin' #base64 encode username, too?
        self.password = '0wlL prfE pqjU 5ru0 OREt oa3V' #base64 encoded version of my pass. Do this somewhere else for each session?
        self.connection = None
        self.tags = None
        self.wp_post_objects = []
        self.connect()
        self.get_all_tags()

    def connect(self):
        self.connection = Client(self.url, self.user, self.password)

    def get_all_tags(self):
        try:
            self.tags = self.connection.call(taxonomies.GetTerms('post_tag'))
        except:
            print("A connection has not been established.")

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
                img_links_from_wp_db = []

                height = "450"
                width = "600"
                thumbnailed = False

                for img in object.image_links:

                    # time.sleep(5)
                    # image = WordPressMedia()
                    # image._def['title'] = '{}_{:02d}.jpg'.format(cl_post_object['cl_id'], cl_post_object['images'].index(img))
                    # image._def['parent'] = int(post_ident)
                    # response = self.connection.call(media.UploadFile(image))
                    # print(response._def['link'])

                    time.sleep(random_sleep)

                    data = {
                    'name': '{}_{:02d}.jpg'.format(object.cl_id, object.image_links.index(img) + 1),
                    'type': 'image/jpeg',
                    # 'date': 'test',
                    'bits': xmlrpc_client.Binary(requests.get(img).content),
                    }
                    # data['bits'] = xmlrpc_client.Binary(requests.get(img).content)

                    response = self.connection.call(media.UploadFile(data))

                    if thumbnailed == False:
                        attachment_id = response['id']
                        thumbnailed = True
                    else:
                        pass

                    img_links_from_wp_db.append(response['url'])

                html_formatted_links = list(
                    map(lambda link: f"<img src={link}>", img_links_from_wp_db)
                    ) # height={height} width={width}>", img_links_from_wp_db))

                print(html_formatted_links)

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
                post.content = str(
                                object.price + '\n' + \
                                object.location + '\n\n' + \
                                object.body_text + '\n' + \
                                ' '.join(html_formatted_links) + '\n\n' + \
                                "Original Post: " + f"<a href={object.orig_url}>{object.orig_url}</a>"
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
                # post.orig_url = object.orig_url
                # # post.make = object.make
                # post.model = object.model
                # post.cl_id = object.cl_id
                # post.__name__ = object.__name__
                # post.price = object.price
                # post.location = object.location
                # post.cl_tags_from_author = object.cl_tags_from_author
                # post.body_text = object.body_text
                # post.when_posted = object.when_posted

                self.wp_post_objects.append(post)

    def post_new_wp_objects(self):
        for post_object in self.wp_post_objects:
                post_object.id = self.connection.call(NewPost(post_object))


"""
    def ping_posts():
        pass
        # get pages in batches of 20
        # offset = 0
        # increment = 20
        # while True:
        #     posts = self.connection.call(GetPosts({'post_status': ['publish', 'draft'], 'number': increment, 'offset': offset}))
        #         # if len(posts) == 0:
        #                 break  # no more posts returned
        #         for post in posts:
        #                 do_something(post)
        #         offset = offset + increment

        # or use this code
        # pub_and_draft_posts = self.connection.call(GetPosts({'post_status': ['publish', 'draft'], 'number': 1000})):

            # for post in pub_and_draft_posts:
                # time.sleep(random_sleep)
                # ping_post = requests.get(post.orig_url)
                # soup_ping = BeautifulSoup(ping_post.text, 'html.parser')
                # if soup_ping.find('div', class_='removed'):
                    # print(soup.find('h2').getText().split('\n')[0])
                    # self.connection.call(DeletePost(post))
                # else:
                    # pass
"""
if __name__ == "__main__":
    pass
