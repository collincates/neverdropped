from wpapi import WPSession

def main():
    """Connect to database, visit original CL URL for each posting in database."""
    wp = WPSession()
    wp.ping_posts()

if __name__ == "__main__":
    main()
