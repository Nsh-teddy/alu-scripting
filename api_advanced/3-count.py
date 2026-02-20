#!/usr/bin/python3
"""
Recursive keyword count from Reddit hot posts
"""
import requests
import re


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively queries Reddit API and counts keywords in hot post titles."""

    if counts is None:
        counts = {}
        # Initialize counts dictionary with lowercase keywords
        for word in word_list:
            counts[word.lower()] = 0

    headers = {'User-Agent': 'python3:keyword-counter:v1.0 (by /u/yourusername)'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100, 'after': after}

    try:
        res = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if res.status_code != 200:
            return  # Invalid subreddit or no posts

        data = res.json().get('data', {})
        posts = data.get('children', [])

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word_lower = word.lower()
                # Match whole words only using regex
                pattern = r'\b{}\b'.format(re.escape(word_lower))
                matches = re.findall(pattern, title)
                counts[word_lower] += len(matches)

        after = data.get('after')
        if after:
            # Recursive call to fetch next page
            count_words(subreddit, word_list, after, counts)
        else:
            # Print results sorted by count descending, then alphabetically
            sorted_counts = sorted(
                ((w, c) for w, c in counts.items() if c > 0),
                key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))

    except Exception:
        return
