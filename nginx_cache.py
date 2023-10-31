import requests

def check_caching_issues(url):
    try:
        response = requests.get(url)
        headers = response.headers

        # Check for common cache-control headers that might indicate caching issues
        cache_control = headers.get('Cache-Control', None)
        if cache_control and 'no-cache' in cache_control:
            print("Cache-Control header is set to no-cache.")
        
        if cache_control and 'no-store' in cache_control:
            print("Cache-Control header is set to no-store.")

        # Check for Set-Cookie header which can affect caching
        if 'Set-Cookie' in headers:
            print("Set-Cookie header found. Cookies might be affecting caching.")
        
        # Check for PHP session ID which can affect caching
        if 'PHPSESSID' in response.text:
            print("PHP session ID found in response. This might affect caching.")

        # Specific checks for WordPress
        if 'X-Powered-By' in headers and 'WordPress' in headers['X-Powered-By']:
            print("WordPress detected. Checking for common issues...")

            # Check for common WordPress plugins/themes that might affect caching
            if 'wp-content/plugins' in response.text or 'wp-content/themes' in response.text:
                print("WordPress plugins or themes detected in the response. They might be affecting caching.")

        print("Analysis complete.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'http://example.com' with your WordPress site URL
check_caching_issues('http://example.com')
