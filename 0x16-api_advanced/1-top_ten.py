#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed
        for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'User-Agent': 'alx-system engineering-devops/1.0/0x16-api'}

    params = {
        "limit": 10,
    }

    response = requests.get(
            url=url, headers=headers,
            allow_redirects=False,
            params=params)

    if response.status_code != 200:
        print("None")
        return
    data = response.json()

    for post in data["data"]["children"]:
        print(f"{post['data']['title']}")
