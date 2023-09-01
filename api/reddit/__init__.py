import os.path
import re
import urllib.request
from random import randint

import requests

import image
from api.googleTranlate import translate_to_croatian
from api.reddit.redditPost import RedditPost

people = ["Mama", "Tata", "Baka", "Deda", "Majko", "Mamica", "Tatica", "Dedica", "Bakica", "Štef", "Jura", "Joža"]


def get_top_posts(subreddit: str):
    url = f"https://www.reddit.com/r/{subreddit}/top/.json"

    querystring = {"t": "day"}

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "sigma based bluepilled alpha 'Christian Bale', 'The Joker', 'Batman', 'u usta ti ga metnem' male"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()["data"]["children"]


def get_post_data(posts: list):
    post_data = []
    for post in posts:
        url = post["data"]["url_overridden_by_dest"]
        title = post["data"]["title"]

        pattern = re.compile("rule", re.IGNORECASE)
        title = pattern.sub("", title)
        title = title.replace("()", "")

        if title == "":
            person = people[randint(0, len(people) - 1)]
            title = f"{person}, pogledaj ovaj bejsd mim!"
        else:
            title = translate_to_croatian(title)

        post_data.append(RedditPost(url, title))

    return post_data


def download_images(posts: list[RedditPost]):
    if not os.path.exists("./imgs/"):
        os.makedirs("./imgs/")

    for i, post in enumerate(posts):
        file_extension = post.url.split(".")[-1]

        if file_extension not in ["png", "jpg", "jpeg"]:
            continue

        filename = f"./imgs/{i}.{file_extension}"

        urllib.request.urlretrieve(post.url, filename)
        post.filename = image.convert_to_jpg(filename)
