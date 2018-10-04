from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
# from wordpress_xmlrpc.methods.users import GetUserInfo

wordpress_url = 'http://localhost:8888/motocl/xmlrpc.php'
username = 'collin'
password = 'lUJijCgtkRZQ&gY4fz'

wp = Client(wordpress_url, username, password)

def newpost(cl_dictionary):
    post = WordPressPost()
    post.title = cl_dictionary['title']
    post.content = cl_dictionary['body_text']
    post.post_status = 'publish'
    wp.call(NewPost(post))


        # 'posting_id': posting_id,
        # 'title': title,
        # 'price': price,
        # 'location': location,
        # 'body_text': body_text,
        # 'when_posted': when_posted,
        # 'original url': orig_url
