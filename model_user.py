from datetime import datetime

class User:
    next_user_id = 100

    def __init__(self, first_name, last_name, user_name):
        self.user_num = User.next_user_id
        User.next_user_id += 1
        self.date_sub = datetime.now()
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name

    def __str__(self):
        return f"""user{self.user_num}: {self.user_name}
name: {self.first_name} {self.last_name}
user created: {self.date_sub}"""