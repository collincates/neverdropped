from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods import taxonomies


# from wordpress_xmlrpc.methods.users import GetUserInfo

wordpress_url = 'http://localhost:8888/motocl/xmlrpc.php'
username = 'collin'
password = '0wlL prfE pqjU 5ru0 OREt oa3V' #base64 encoded version of my pass


wp = Client(wordpress_url, username, password)

def new_wp_post(posting_data):
    # check if a cl_id already exists in the WP DB. If so, pass.
    tag_list = [tag.name for tag in [entry for entry in wp.call(taxonomies.GetTerms('post_tag'))]]
    if posting_data['cl_id'] in tag_list:
        print('{} already in database'.format(posting_data['cl_id']))
        pass
    else:
        post = WordPressPost()
        post.title = posting_data['title']
        post.content = posting_data['body_text']
        print('{} this work?'.format(posting_data['cl_id']))
        post.terms_names = {
            'post_tag': [posting_data['cl_id']]
        }
        print('this work?')
        post.post_status = posting_data['post_status']
        wp.call(NewPost(post))


        # 'posting_id': posting_id,
        # 'title': title,
        # 'price': price,
        # 'location': location,
        # 'body_text': body_text,
        # 'when_posted': when_posted,
        # 'original url': orig_url

new_wp_post({'title': 'new one', 'body_text': 'this isthe body text', 'post_status': 'publish', 'cl_id': '012398'})
