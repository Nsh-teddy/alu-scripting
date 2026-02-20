#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.
    If the subreddit is invalid, prints None.
    """
    # Use a very specific User-Agent to avoid being throttled/blocked
    headers = {
        'User-Agent': 'MyRedditBot/1.0 (by nshimyumurwa)'
    }

    # The URL for the hot posts
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set limit to 10
    params = {'limit': 10}

    try:
        # allow_redirects=False is crucial for invalid subreddits
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Only proceed if the status is exactly 200 OK
        if response.status_code == 200:
            # We use .get() repeatedly to avoid KeyErrors
            data = response.json().get('data', {})
            children = data.get('children', [])

            # Check if we actually got children back
            if not children:
                print(None)
                return

            for post in children:
                print(post.get('data', {}).get('title'))
        else:
            # This catches 404, 302, 429, etc.
            print(None)

    except Exception:
        # Any other error (network, JSON parsing) prints None
        print(None)
