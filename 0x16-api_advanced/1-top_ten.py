#!/usr/bin/python3
"""
Module to query the Reddit API for the top 10 hot posts of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Python/requests'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        for post in posts[:10]:
            print(post.get('data', {}).get('title', None))

    except requests.exceptions.RequestException as e:
        print(None)
        print("Exception: {}".format(e))

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print("Status Code:", response.status_code)  # Debugging line
        print("Response Content:", response.text)  # Debugging line

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])

        for post in posts[:10]:
            print(post.get('data', {}).get('title', None))

    except requests.exceptions.RequestException as e:
        print(None)
        print("Exception:", e)  # Debugging line
