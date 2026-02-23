#!/usr/bin/python3
"""
Query Reddit API to get top 10 hot posts from a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "python:subreddit.top10:v1.0.0 (by /u/holberton_student)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except Exception:
        print(None)
