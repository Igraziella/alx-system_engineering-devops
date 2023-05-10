#!/usr/bin/python3
"""
A recursive function that Queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[]):
    """ Returns a list containing the titles of all hot articles
        for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'alx-system_engineering-devops/\
            1.0/0x16-api_advanced'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    for post in posts:
        title = post['data']['title']
        hot_list.append(title)

        if data['data']['after'] is not None:
            after = data['data']['after']
            return recurse(subreddit, hot_list=hot_list, after=after)
        else:
            return hot_list
    else:
        return None
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")
    else:
        print("None")
