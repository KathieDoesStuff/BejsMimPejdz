import os
from pathlib import Path

import spyl
from instagrapi import Client
from api.reddit import RedditPost
from dotenv import load_dotenv

load_dotenv()

cl = Client()
cl.login(os.getenv("INSTA_USERNAME"), os.getenv("INSTA_PASSWORD"))
logger = spyl.Logger()


def post_images(posts: list[RedditPost]):
    for post in posts:
        try:
            cl.photo_upload(Path(post.filename), post.title)
        except Exception as e:
            logger.log_error(e)
