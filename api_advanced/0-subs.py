#!/usr/bin/python3
"""
0-subs
Returns the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Query Reddit API and return number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/anonymous)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            return response.json().get("data").get("subscribers")
        else:
            return 0
    except Exception:
        return 0
