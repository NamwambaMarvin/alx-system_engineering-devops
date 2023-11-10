#!/usr/bin/python3
"""
    This module queries reddit api
"""
import requests as r
import json
# Setup custom user agent
headers = {

        "User-Agent": "Mozilla/5.0"

        }


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    if type(subreddit) is not str:
        return (0)
    try:
        data = r.get(url, headers=headers).json()
        print(data['data']['subscribers'])
    except KeyError:
        return (0)
