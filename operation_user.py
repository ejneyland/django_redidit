from model_user import User


class UserOperation:
    def create_user(self, email, phone, first_name, last_name, user_name):
        new_user = User(
            email=email,
            phone=phone,
            first_name=first_name,
            last_name=last_name,
            user_name=user_name,
        )
        return new_user

    def read_user(self, user):
        return str(user)

    def update_user_name(self, user: User, new_user_name):
        user.user_name = new_user_name


# ---------------------------------------------
# FOR DEVELOPMENT AND TROUBLESHOOTING
# ---------------------------

# user_ops = UserOperation()

# user4 = user_ops.create_user(
#     email="daisythomas@gmail.com",
#     phone="0413777999",
#     first_name="Daisy",
#     last_name="Thomas",
#     user_name="daisy_chain",
# )

# user5 = user_ops.create_user(
#     email="thegtrain@gmail.com",
#     phone="0412345678",
#     first_name="Fraser",
#     last_name="Gehrig",
#     user_name="tootTooT_itsthe_GTrain",
# )

# print(user5)

# user_ops.update_user_name(user5, "tootoot_itsthe_gtrain")

# print(user5)
