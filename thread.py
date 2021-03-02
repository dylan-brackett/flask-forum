from post import Post

class Thread:
    posts = []

    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
