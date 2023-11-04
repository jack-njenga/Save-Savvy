#!/usr/bin/env python3
"""
THis is the user model
"""
from models.base import BaseModel, Base
from models import *

class User(BaseModel, Base):
    """
    user class
    """
    __tablename__ = "users"
    default = "NAN"
    first_name = Column(String(100), nullable=False, default=default)
    last_name = Column(String(100), nullable=False,         default=default)
    email = Column(String(60), nullable=False,
                   default=default)
    password = Column(String(60), nullable=False, default=default)
    dob = Column(String(60), nullable=False, default=default)
    gender = Column(String(28), nullable=False, default=default)

    def __init__(self, *args, **kwargs):
        """
        """
        super().__init__(*args, **kwargs)

    def get(email="", pwd=""):
        """
        get a user by email
        """
        from models.engine import Storage

        users = Storage.get_user_by_email(email)
        filters = ["first_name", "last_name", "email", "gender"]
        user_fogort_pwd = False
        users_list = []

        if isinstance(users, list):
            if len(users) > 1:
                print("--A--:(ALERT) Users with same Email Detected")
                # logging the alert :

            for user in users:
                user_dict = {}
                # print(user.to_dict(hide=False))
                for key, val in user.to_dict(hide=False).items():
                    if key in ["password"]:
                        if val == pwd:
                            # print(f"{key}: {val}")
                            pass
                        else:
                            user_fogort_pwd = True
                            user_dict = {}
                            break
                    if key in filters:
                        user_dict[key] = val
                if len(list(user_dict.keys())) > 0:
                    users_list.append(user_dict)
                    # print(users_list)
        if len(users_list) > 0:
            if len(users_list) > 1:
                print("--A--(ALERT) Users with Same Email & Password Detected")
                # logging the alert
                # return {"user": "!"}
            return users_list[0]
        else:
            if user_fogort_pwd is True:
                return {"user": "forgot_pwd"}
            return {"user": False}


