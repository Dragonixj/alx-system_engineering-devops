#!/usr/bin/python3
"""Queries the reddit api and returns number of suscribers"""

import requests


def top_ten(subreddit):
    """Print the title of the top 10 hottest posts on a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    sub_top_ten = requests.get(
        url,
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
        params={"limit": 10},
    )

    if sub_top_ten.status_code == 404:
        print("None")
        return
    results = sub_top_ten.json().get("data")
    [print(child.get("data").get("title")) for child in results.get("children")]
