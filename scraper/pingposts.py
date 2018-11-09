from wpapi import WPSession

def main():
    wp = WPSession()
    wp.ping_posts()

if __name__ == "__main__":
    main()
