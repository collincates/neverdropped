from clapi import CLFactory
from wpapi import WPSession

def main():
    # at 5pm PST:
    wp_session = WPSession()
    print("started wp session")
    # print(wp_session.tags)
    cl_factory = CLFactory()
    # print("made cl factory")
    cl_factory.make_rss_feeds()
    # print("made rss feeds")
    # print([rss_object.rss_url for rss_object in cl_factory.rss_objects_to_scrape])
    cl_factory.get_new_cl_posts_from_rss_feeds(compare_to=wp_session.tags)
    # print("got new posts from rss feeds")
    # print(cl_factory.rss_objects_to_scrape)
    # print([rss_object.posting_urls for rss_object in cl_factory.rss_objects_to_scrape])
    # cl_factory.cull_new_posts_from_rss_feeds(compare_to=wp_session.tags)
    # print("made new post objects")
    # for post in cl_factory.new_cl_postings:
    #     print(
    #     post.orig_url,
    #     post.make,
    #     post.model,
    #     post.cl_id,
    #     post.__name__,
    #     post.title,
    #     post.price,
    #     post.location,
    #     post.cl_tags_from_author,
    #     post.body_text,
    #     post.when_posted,
    #     post.image_links
    #     )
    wp_session.make_new_wp_objects_from(cl_factory.new_cl_postings)
    # print(wp_session.wp_post_objects)
    wp_session.post_new_wp_objects()
    print(f"Posted {[post_object.id for post_object in wp_session.wp_post_objects]}")


    # at 5am PST:
    # ping if posts active. if not, delete.

if __name__ == "__main__":
    main()
