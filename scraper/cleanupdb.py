from wpapi import WPSession

def main():
    """Connect to database and drop all items with post_status='trash'."""
    wp = WPSession()
    wp.cleanup()

if __name__ == "__main__":
    main()
