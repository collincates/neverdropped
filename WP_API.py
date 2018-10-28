from wordpress_xmlrpc import Client, WordPressPost, WordPressMedia
from wordpress_xmlrpc.methods.posts import NewPost, GetPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import taxonomies, media
import requests
import time
# import base64


# from wordpress_xmlrpc.methods.users import GetUserInfo

wordpress_url = 'http://localhost:8888/motocl/xmlrpc.php'
username = 'collin'
password = '0wlL prfE pqjU 5ru0 OREt oa3V' #base64 encoded version of my pass


wp = Client(wordpress_url, username, password)

def new_wp_post(posting_data, post_status='draft'):
    # check if a cl_id already exists in the WP DB. If so, pass.
    tag_list = [tag.name for tag in [entry for entry in wp.call(taxonomies.GetTerms('post_tag'))]]
    if posting_data['cl_id'] in tag_list:
        print('{} already in database'.format(posting_data['cl_id']))
        pass
    # if it's a new cl_id, create a blog post for it.
    else:
        # images upload
        wp_db_img_links = []

        height = "450"
        width = "600"
        thumbnailed = False

        for img in posting_data['images']:
            """
            time.sleep(5)
            image = WordPressMedia()
            image._def['title'] = '{}_{:02d}.jpg'.format(posting_data['cl_id'], posting_data['images'].index(img))
            image._def['parent'] = int(post_ident)
            response = wp.call(media.UploadFile(image))
            print(response._def['link'])


            """
            time.sleep(5)
            data = {
            'name': '{}_{:02d}.jpg'.format(posting_data['cl_id'], posting_data['images'].index(img) + 1),
            'type': 'image/jpeg',
            }
            data['bits'] = xmlrpc_client.Binary(requests.get(img).content)

            response = wp.call(media.UploadFile(data))

            if thumbnailed == False:
                attachment_id = response['id']
                thumbnailed = True
            else:
                pass

            wp_db_img_links.append(response['url'])

        html_formatted_links = list(
            map(lambda link: f"<img src={link}>", wp_db_img_links)
            ) # height={height} width={width}>", wp_db_img_links))

        print(html_formatted_links)



        post = WordPressPost()

        post.title = posting_data['title']

        post.thumbnail = attachment_id

        post.content = str(
                        posting_data['price'] + '\n' + \
                        posting_data['location'] + '\n\n' + \
                        posting_data['body_text'] + '\n' + \
                        ' '.join(html_formatted_links) + '\n\n' + \
                        "Original Post: " + f"<a href={posting_data['original_url']}>{posting_data['original_url']}</a>"
        )

        post.terms_names = {
            'post_category': [posting_data['make']]

            'post_tag': [posting_data['cl_id'], posting_data['location']], #other terms from cl_author_tags]

        }
        post.post_status = post_status

        post_ident = wp.call(NewPost(post))




{
'cl_id': cl_id,
'title': title,
'price': price,
'location': location,
# pass cl_tags_from_author
'body_text': body_text,
'when_posted': when_posted,
'original_url': orig_url,
'images': images,
}


def ping_posts():
    pass
    # get pages in batches of 20
    # offset = 0
    # increment = 20
    # while True:
    #     posts = wp.call(GetPosts({'post_status': ['publish', 'draft'], 'number': increment, 'offset': offset}))
    #         # if len(posts) == 0:
    #                 break  # no more posts returned
    #         for post in posts:
    #                 do_something(post)
    #         offset = offset + increment

    # or use this code
    # pub_and_draft_posts = wp.call(GetPosts({'post_status': ['publish', 'draft'], 'number': 1000})):

        # for post in pub_and_draft_posts:
            # time.sleep(random_sleep)
            # ping_post = requests.get(post.orig_url)
            # soup_ping = BeautifulSoup(ping_post.text, 'html.parser')
            # if soup_ping.find('div', class_='removed'):
                # print(soup.find('h2').getText().split('\n')[0])
                # wp.call(DeletePost(post))
            # else:
                # pass

if __name__ == "__main__":
    new_wp_post({'title': 'new one', 'body_text': 'this isthe body text', 'post_status': 'publish', 'cl_id': '012396'})
