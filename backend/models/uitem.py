#!/usr/bin/env python3
"""
Data Transform modules
"""
from models import *
from models.base import BaseModel, Base
from models.item import Item

class UItem(BaseModel, Base):
    """
    Transform Class
    """

    __tablename__ = "uitems"
    type = Column(String(64), nullable=False, default="-item-")
    count = Column(Integer, nullable=False, default=0)
    latest_update = Column(DateTime)
    earliest_update = Column(DateTime)
    min_price = Column(Integer)
    median_price = Column(Integer)
    max_price = Column(Integer)
    mean_price = Column(Integer)
    mode = Column(String(64))
    freq = Column(String(96))
    nunique_price = Column(Integer)

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        new_kwargs = {}
        if kwargs:
            req = ['type', 'count', 'latest_update', 'earliest_update', 'min_price', 'median_price', 'max_price', 'mean_price', 'mode', 'freq', 'nunique_price']
            for key, val in kwargs.items():
                if key in req:
                    new_kwargs[key] = val
                else:
                    print(f"--A--(ALERT): {key} is not required droping it...")
                    pass
            # print("="*40)
            # print(new_kwargs)
            # print("="*40)
            super().__init__(*args, **new_kwargs)

    def get_all_uitems(self, get_all=False):
        """
        returns all items in uitems table
        """
        from models.engine import Storage

        uitems = Storage.get_all_uitems(get_all=get_all)

        return uitems

    def get_uitems(self, item=""):
        """returns the unique uitem"""
        from models.engine import Storage

        uitem = Storage.get_uitems_by_type(item)
        return uitem


