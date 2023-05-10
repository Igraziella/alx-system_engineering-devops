#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed
        for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/top/.json"
    headers = {'User-Agent': 'alx-system engineering-devops/1.0/0x16-api'}

    params = {
        "limit": 10,
    }

    response = requests.get(
            url=url, headers=headers,
            allow_redirects=False,
            params=params)

    data = response.json()

    if "data" in data and "children" in data["data"]:
        # Iterate through the top posts, print and post number and title
        for i, post in enumerate(data["data"]["children"], start=1):
            print(f"{i}: {post['data']['title']}")
    else:
        print("None")
