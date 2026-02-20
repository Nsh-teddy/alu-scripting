#!/usr/bin/python3
"""
Recursive function to fetch all hot post titles from a subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "python:alu.api.advanced:v1.0 (by /u/anonymous)"
    }

    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    if not data:
        return None

    children = data.get("children")
    after = data.get("after")

    for post in children:
        hot_list.append(post.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
