import os
from pathlib import Path

import spyl
from instagrapi import Client
from api.reddit import RedditPost

cl = Client()
logger = spyl.Logger()


def post_images(posts: list[RedditPost]):
    cl.login(os.getenv("INSTA_USERNAME"), os.getenv("INSTA_PASSWORD"))

    for post in posts:
        try:
            cl.photo_upload(Path(post.filename), post.title)
        except Exception as e:
            logger.log_error(e)
