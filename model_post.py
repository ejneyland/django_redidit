from datetime import datetime
from model_user import User


class Post:
    next_post_id = 10000

    # using type 'hint' for author, documentation purposes only
    def __init__(self, author: "User", title, body):
        self.post_id = Post.next_post_id
        Post.next_post_id += 1
        self.date_pub = datetime.now()
        self.author = author
        self.title = title
        self.body = body

    def __str__(self):
        return f"""post id: {self.post_id}
date/time: {self.date_pub}
\n{self.author.user_name}:  {self.title}
\n{self.body}\n"""