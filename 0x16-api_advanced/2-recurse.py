#!/usr/bin/python3
"""
Using reddit's API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returning top ten post titles recursively"""
    user_agent = {"User-Agent": "My-User-Agent"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {"after": after}
    sub_info = requests.get(
        url,
        params=parameters,
        headers=user_agent,
        allow_redirects=False,
    )

    if sub_info.status_code == 200:
        after_data = sub_info.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = sub_info.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None
