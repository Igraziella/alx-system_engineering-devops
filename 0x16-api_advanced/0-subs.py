#!/usr/bin/python3
"""  a function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ Returns the total number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about/.json".format(subreddit)
    headers = {"User-Agent": "0x16-api_advanced:project: v1.0.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json()
    subscribers = data.get("data", {}).get("subscribers", 0)

    return subscribers
