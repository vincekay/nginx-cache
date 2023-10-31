import requests
import sys

def check_cache_issues(url):
    try:
        response = requests.get(url)

        # Check for cookies
        cookies = response.cookies
        for cookie in cookies:
            if 'wordpress_logged_in' in cookie.name:
                print(f"Cache might be blocked by WordPress login cookie: {cookie.name}")

        # Check for cache-control headers
        cache_control = response.headers.get('Cache-Control')
        if cache_control and ('no-cache' in cache_control or 'no-store' in cache_control or 'private' in cache_control):
            print(f"Cache might be blocked by Cache-Control header: {cache_control}")

        # Check for set-cookie headers
        set_cookie_headers = response.headers.get('Set-Cookie', '')
        if 'PHPSESSID' in set_cookie_headers:
            print("PHP session found, might block cache.")

        if set_cookie_headers:
            print(f"Set-Cookie header found, might block cache: {set_cookie_headers}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <wordpress_site_url>")
    else:
        url = sys.argv[1]
        check_cache_issues(url)
