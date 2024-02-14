#!/usr/bin/python3
"""Queries the reddit api and returns number of suscribers"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers to the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    sub_info = requests.get(
        url,
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
    )

    if sub_info.status_code != 200:
        return 0
    data = sub_info.json().get("data")
    if data is None:
        return 0
    return data.get("subscribers", 0)
