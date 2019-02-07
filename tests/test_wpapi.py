import unittest
import os
from scraper.wpapi import WPSession
from wordpress_xmlrpc.methods.taxonomies import NewTerm#, GetTerms
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost, DeletePost, GetPosts

class WPSessionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create session / database connection
        cls.session = WPSession()

        # Initialize tag list for testing session
        cls.session.tags = []

        # Create dummy posts for tests
        number_of_test_post_objects = 5

        for id_num in range(number_of_test_post_objects):
            post = WordPressPost()
            post.id = None
            post.title = f'{id_num} title'
            post.content = (f'{id_num} content')
            post.terms_names = {
                'category': [f'{id_num} make'],
                'post_tag': [f'{id_num} cl_id', f'{id_num} model', f'{id_num} cl_tags_from_author']
            }
            post.custom_fields = [
                {'key': 'original_posting_url', 'value': f'{id_num} orig_url'},
                {'key': 'make', 'value': f'{id_num} make'},
                {'key': 'model', 'value': f'{id_num} model'},
                {'key': 'cl_id', 'value': f'{id_num} cl_id'},
                {'key': 'name', 'value': f'{id_num} cl_id'},
                {'key': 'title', 'value': f'{id_num} title'},
                {'key': 'price', 'value': f'{id_num} price'},
                {'key': 'location', 'value': f'{id_num} location'},
                {'key': 'cl_tags_from_author', 'value': f'{id_num} cl_tags_from_author'},
                {'key': 'body_text', 'value': f'{id_num} body_text'},
                {'key': 'when_posted', 'value': f'{id_num} when_posted'},
                {'key': 'cl_image_links', 'value': f'{id_num} image_links'},
                ]

            cls.session.wp_post_objects.append(post)
            cls.session.tags.extend([tag for tag_list in [post.terms_names['post_tag']] for tag in tag_list])

    def test_connect(self):
        self.assertIsNotNone(self.session.connection)

    def test_get_all_tags(self):
        """Assert length of tag list matches predicted quantity of tags."""
        print(self.session.tags)
        self.assertEqual(
            len(self.session.tags),
            (3 * len(self.session.wp_post_objects)) #3 tags added by default
        )

    def test_post_new_wp_objects(self):
        for post_object in self.session.wp_post_objects:
                post_object.id = self.session.connection.call(NewPost(post_object))

    def test_post_title(self):
        for post_object in self.session.wp_post_objects:
            self.assertEqual(
                post_object.title,
                f'{self.session.wp_post_objects.index(post_object)} title'
            )

    def test_post_content(self):
        for post_object in self.session.wp_post_objects:
            self.assertEqual(
                post_object.content,
                f'{self.session.wp_post_objects.index(post_object)} content'
            )

    def test_post_terms_names(self):
        for post_object in self.session.wp_post_objects:
            self.assertEqual(
                post_object.terms_names['category'],
                [f'{self.session.wp_post_objects.index(post_object)} make']
            )
            self.assertEqual(
                post_object.terms_names['post_tag'],
                        [
                        f'{self.session.wp_post_objects.index(post_object)} cl_id',
                        f'{self.session.wp_post_objects.index(post_object)} model',
                        f'{self.session.wp_post_objects.index(post_object)} cl_tags_from_author'
                        ]
            )

    @classmethod
    def tearDownClass(cls):
        """Drop all dummy posts used during tests."""
        for post in cls.session.wp_post_objects:
            cls.session.connection.call(DeletePost(post.id))

        # Test cleanup() method to assert that all dummy test posts
        # have been trashed and are dropped from database.
        cls.session.cleanup()

        # Assert that no items remain in WordPress trash / have been dropped from database.
        self.assertFalse(self.session.connection.call(GetPosts({'post_status': 'trash'})))
