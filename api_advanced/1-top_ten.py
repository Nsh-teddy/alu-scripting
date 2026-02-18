#!/usr/bin/python3
"""
1-top_ten
Prints the titles of the first 10 hot posts of a subreddit
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {
        "User-Agent": "python:alu-scripting:v1.0 (by /u/anonymous)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if subreddit exists
        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)
