#!/usr/bin/env python3
"""
-id
-type
-name
-desc
-price
-link
"""
from models.base import BaseModel, Base
from models import *

class Item(BaseModel, Base):
    """
    Item class
    """
    __tablename__ = "items"

    type = Column(String(64), nullable=False, default="-item-")
    category = Column(String(200), nullable=False, default="-category-")
    name = Column(String(256), nullable=False, default="nan")
    description = Column(String(256), nullable=False, default="nan")
    price = Column(String(64), nullable=False, default="-0-")
    link = Column(String(256), nullable=False, default="https:/www.jacknjenga.tech")

    def __init__(self, *args, **kwargs):
        """Initialzation"""
        new_kwargs = {}
        if kwargs:
            for key, val in kwargs.items():
                if key in ["type", "name", "price"]:
                    if val and len(val):
                        new_kwargs[key] = val
                elif key in ["category", "description", "link"]:
                    new_kwargs[key] = val
                else:
                    pass
        else:
            pass
            # print("--W--(WARN): No Data given using default values")
        super().__init__(*args, **new_kwargs)

    def get_item(self, *args, **kwargs):
        """
        returns the item of a specific type
        """
        from models.engine import Storage

        item = ""
        if args:
            if len(args) > 1:
                print("--W--(WARN): One Item at a time pls")
            item = args[0].replace(" ", "+")

        if kwargs:
            keys = list(kwargs.keys())
            if len(keys) > 1:
                print("--W--(WARN): One Item at a time pls")
            item = str(kwargs[keys[0]]).replace(" ", "+")
        items = Storage.get_items_by_type(item)
        if len(items) == 0:
            item = item.replace("+", " ")
            items = Storage.get_items_by_type(item)
        # print(f"{item}: {items}")
        return items

    def get_all_items(self):
        """
        returns all items
        """
        from models.engine import Storage

        items = Storage.get_all_items()
        return items

    def get_item_by_id(self, id=""):
        """returns an item of that id"""
        from models.engine import Storage

        items = Storage.get_items_by_id(id)
        if len(items) > 1:
            print("--W--(WARN): ----{len(all_unqs)}")
        return items
