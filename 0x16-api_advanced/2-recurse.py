#!/usr/bin/python3
"""
Query the Reddit API for the titles of all hot articles in a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot
    articles for a given subreddit. If no results are found, returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Python/requests'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        posts = data.get('children', [])

        if not posts:
            return hot_list

        hot_list.extend([post.get('data', {}).get('title') for post in posts])
        after = data.get('after')

        if after:
            next_url = "{}?after={}".format(url, after)
            return recurse(subreddit, hot_list)

        return hot_list

    except requests.exceptions.RequestException:
        return None
