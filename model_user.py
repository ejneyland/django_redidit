from datetime import datetime


class User:
    existing_ids = set()
    next_user_id = 100

    def __init__(self, email, phone, first_name, last_name, user_name):
        self.user_num = User.next_user_id
        User.next_user_id += 1
        # DATE string-format-time,  DD/MM/YYYY HH:MM:SS
        self.date_sub = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name

    def __str__(self):
        return f"""   user:  {self.user_name} (#{self.user_num})
   name:  {self.first_name} {self.last_name}
  email:  {self.email}
  phone:  {self.phone}
created:  {self.date_sub}"""
