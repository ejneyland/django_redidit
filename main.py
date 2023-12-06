from model_user import User
from model_post import Post

# a list of posts initialised
posts = []

# creating three User instances
user1 = User(
    email="leejenkins@gmail.com",
    phone="0419111222",
    first_name="Leeroy",
    last_name="Jenkins",
    user_name="lee_roooooy"
)
user2 = User(
    email="friendlyneighbour@hotmail.com",
    phone="0413222333",
    first_name="Mary",
    last_name="Jane",
    user_name="mary_jane_xx"
)
user3 = User(
    email="suzanne@outlook.com",
    phone="0409333444",
    first_name="Big",
    last_name="Suze",
    user_name="sophisticatedwoman"
)

# printing the User instances
print("\n")
print(str(user1) + "\n")
print(str(user2) + "\n")
print(str(user3) + "\n")

# creating three Post instances, one for each User
post1 = Post(
    author=user1, title="First Post", body="This is the body of the first post"
)
post2 = Post(
    author=user2, title="Second Post", body="This is the body of the second post"
)
post3 = Post(
    author=user3, title="Third Post", body="This is the body of the third post"
)

# printing the Post instances
print(post1)
print(post2)
print(post3)
