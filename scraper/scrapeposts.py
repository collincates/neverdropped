import logging
from clapi import CLFactory
from wpapi import WPSession


logging.basicConfig(
    filename='../scraper.log',
    filemode='a',
    format='%(asctime)s - %(module)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d - %H:%M:%S',
    level=logging.INFO
)

def main():
    """
    Establish connection with WordPress database and retrieve all current records.
    Cull new CL postings (by comparison of current records) and pass them to WordPress API.
    Use WordPress API to insert new posting records to database.

    """

    wp_session = WPSession()
    logging.INFO("Started WordPress session")
    cl_factory = CLFactory()
    cl_factory.make_rss_feeds()
    cl_factory.get_new_cl_posts_from_rss_feeds(compare_to=wp_session.tags)
    wp_session.make_new_wp_objects_from(cl_factory.new_cl_postings)
    wp_session.post_new_wp_objects()
    logging.info(f"Posted {[post_object.id for post_object in wp_session.wp_post_objects]}")

if __name__ == "__main__":
    main()
