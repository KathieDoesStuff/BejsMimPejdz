from api import reddit
from api import instagram

postsRaw = reddit.get_top_posts("196")
posts = reddit.get_post_data(postsRaw)

reddit.download_images(posts)

instagram.post_images(posts)
