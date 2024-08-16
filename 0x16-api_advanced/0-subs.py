#!/usr/bin/python3
"""
Module to query the Reddit API for the number of subscribers of a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/requests'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json().get('data', {})
        return data.get('subscribers', 0)

    except requests.exceptions.RequestException:
        return 0
