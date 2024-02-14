#!/usr/bin/python3
"""Queries the reddit api and returns number of suscribers"""

from requests import get


def number_of_subscribers(subreddit):
    """returns the number of subscribers to the subreddit"""
    sub_info = get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False,
    )

    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
