#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the total number of subscribers
        for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'alx-system_engineering-devops/\
            1.0/0x16-api_advanced'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    subscribers = data['data']['subscribers']

    if subreddit is None or type(subreddit) is not str:
        return 0
    else:
        return subscribers
