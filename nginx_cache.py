import urllib.request

def check_caching_issues(url):
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            headers = response.getheaders()

            # Convert headers list of tuples to a dictionary for easier access
            headers_dict = dict(headers)

            # Check for common cache-control headers that might indicate caching issues
            cache_control = headers_dict.get('Cache-Control', None)
            if cache_control and ('no-cache' in cache_control or 'no-store' in cache_control):
                print("Cache-Control header is set to no-cache or no-store.")

            # Check for Set-Cookie header which can affect caching
            if 'Set-Cookie' in headers_dict:
                print("Set-Cookie header found. Cookies might be affecting caching.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'http://example.com' with your WordPress site URL
check_caching_issues('http://example.com')
