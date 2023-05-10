#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed
        for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'alx-system_engineering-devops/\
            1.0/0x16-api_advanced'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for i, post in enumerate(posts[:10], 1):
            title = post['data']['title']
            print(f"{i}. {title}")
        else:
            print("None")
