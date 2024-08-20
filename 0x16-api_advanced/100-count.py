#!/usr/bin/python3
"""
Module to query the Reddit API and count occurrences of keywords in hot posts.
"""
import requests
import re


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries the Reddit API and counts the occurrences of keywords
    in hot posts for a given subreddit. Prints the results sorted by count in
    descending order, and alphabetically for ties.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Python/requests'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json().get('data', {})
        posts = data.get('children', [])
        after = data.get('after')

        if not posts:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
            return

        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in counts:
                count = len(re.findall(r'\b{}\b'.format(re.escape(word)), title))
                counts[word] += count

        if after:
            count_words(subreddit, word_list, counts, after)

    except requests.exceptions.RequestException:
        return
