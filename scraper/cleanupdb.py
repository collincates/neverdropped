from wpapi import WPSession

def main():
    wp = WPSession()
    wp.cleanup()

if __name__ == "__main__":
    main()
