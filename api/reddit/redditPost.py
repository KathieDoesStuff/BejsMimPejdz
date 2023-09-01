from dataclasses import dataclass


@dataclass
class RedditPost:
    url: str
    title: str
    filename: str = None
