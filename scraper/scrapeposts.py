from clapi import CLFactory
from wpapi import WPSession

def main():
    """
    Establish connection with WordPress database and retrieve all current records.
    Cull new CL postings (by comparison of current records) and pass them to WordPress API.
    Use WordPress API to insert new posting records to database.

    """

    wp_session = WPSession()
    print("started wp session")
    cl_factory = CLFactory()
    cl_factory.make_rss_feeds()
    cl_factory.get_new_cl_posts_from_rss_feeds(compare_to=wp_session.tags)
    wp_session.make_new_wp_objects_from(cl_factory.new_cl_postings)
    wp_session.post_new_wp_objects()
    print(f"Posted {[post_object.id for post_object in wp_session.wp_post_objects]}")

if __name__ == "__main__":
    main()
