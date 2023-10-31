import requests

def check_caching_issues(url):
    try:
        response = requests.get(url)
        headers = response.headers

        # Check for cache-control headers that might prevent caching
        cache_control = headers.get('Cache-Control', None)
        if cache_control and ('no-cache' in cache_control or 'no-store' in cache_control):
            issues.append("Cache-Control header is set to no-cache or no-store.")

        # Check for Set-Cookie header
        if 'Set-Cookie' in headers:
            issues.append("Set-Cookie header found. Cookies might be preventing caching.")

        # Check for PHP session ID
        if 'PHPSESSID' in html_content:
            issues.append("PHP session ID found in response. This might prevent caching.")

        # Check for common WordPress plugins or themes
        for script_tag in soup.find_all('script'):
            src = script_tag.get('src', '')
            if 'wp-content/plugins' in src or 'wp-content/themes' in src:
                issues.append(f"WordPress plugin or theme detected in script source: {src}")

        # Reporting the issues
        if issues:
            print("Potential issues detected:")
            for issue in issues:
                print(f"- {issue}")
        else:
            print("No obvious caching issues detected.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'http://example.com' with your WordPress site URL
analyze_site('http://example.com')
