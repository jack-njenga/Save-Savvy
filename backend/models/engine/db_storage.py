#!/usr/bin/env python3
"""
DB Storage engine
"""
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base import BaseModel, Base
from models.user import User
from models.item import Item
from models.uitem import UItem

class DBStorage():
    """
    DbStorage class
    """
    __session = None
    __engine = None

    def __init__(self, *args, **kwargs):
        """
        initialization
        """
        db = getenv("SAVY_DB", "savy_db")
        user = getenv("SAVY_USER", "savy_user")
        host = getenv("SAVY_HOST", "localhost")
        pwd = getenv("SAVY_PWD", "Savy-2146")

        url = f"mysql+mysqlconnector://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(url)

    def reload(self):
        """
        creates a new session
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def save(self, obj):
        """
        adds an obj to the session
        then saves it to the database
        """
        self.__session.add(obj)
        self.__session.commit()

    def get_user_by_email(self, email=""):
        """
        Retruns a user give an email
        """
        users = self.__session.query(User).filter(User.email == email).all()

        return users

    def get_items_by_id(self, id=""):
        """
        returns the item asked
        """
        items = self.__session.query(Item).filter(Item.id == id).all()
        return items

    def get_items_by_type(self, item=""):
        """
        returns the item asked
        """
        items = self.__session.query(Item).filter(Item.type == item).all()

        return items

    def get_all_items(self):
        """
        returns all items
        """
        items = self.__session.query(Item).all()

        return items

    def get_uitems_by_type(self, type=""):
        """
        """
        all_unqs = self.__session.query(UItem).filter(UItem.type == type).all()
        return all_unqs[0]

    def get_all_uitems(self, get_all=False):
        """
        Returns all items
        """
        from models.ml.transformer import Transformer

        uits = []
        tsfm = Transformer()
        unqs = tsfm.get_unique_items()

        for unq in unqs:
            # unq = unq.replace(" ", "+")
            # print(unq)
            if get_all is True:
                items = self.__session.query(UItem).all()
                return items
            all_unqs = self.__session.query(UItem).filter(UItem.type == unq).all()
            if len(all_unqs) > 1:
                # print(f"--W--(WARN): ----{len(all_unqs)}")
                pass
            if all_unqs:
                uits.append(all_unqs[0])

        # print(its[0].to_dict())

        # items = self.__session.query(UItem).all()

        return uits



