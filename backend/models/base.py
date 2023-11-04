#!/usr/bin/env python3
"""
This is the Base Model from which all other models inherit
"""
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4


fmt = "%Y-%m-%dT%H:%M:%S"
Base = declarative_base()

class BaseModel():
    """
    Base Model class
    """
    now = datetime.now()
    id = Column(String(40), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=now, nullable=False)
    updated_at = Column(DateTime, default=now, nullable=False)

    def __init__(self, *args, **kwargs):
        """
        inintialization
        """
        now = datetime.now()
        self.id = str(uuid4())
        self.created_at = now
        self.updated_at = now
        if args:
            pass
        if kwargs:
            kwargs = self.verify_kwargs(kwargs)
            for key, val in kwargs.items():
                setattr(self, key, val)


    def verify_kwargs(self, kwargs={}):
        """
        verifys if kwargs in __dict__
        """
        if self.confirm_io(kwargs, "dict"):
            new_kwargs = {}
            reserved_att = list(self.__dict__.keys())
            reserved_att.append("__class__")

            for key, val in kwargs.items():
                if key not in reserved_att:
                    new_kwargs[key] = val
            if self.confirm_io(kwargs, "dict"):
                return new_kwargs
        else:
            print("--E--: input not as expected")
            # add an error log

    def confirm_io(self, *args, **io):
        """
        This one confirms the type of input/output expected
        """
        if args:
            if len(args) > 0:
                key = args[0]
                if len(args) > 1:
                    val = args[1]
                    if len(args) > 2:
                        print("--R--(REJECT) Only 2 args at a time")
                else:
                    print("--W--: (WARN) Provide at least 2 args(default = bool)")
                    val = bool
                if type(val) is str:
                    try:
                        val = eval(val)
                    except Exception as e:
                        print("--E--(ERR) Could not evaluate to obj", e)
                        val = bool
                # eg: confirm_io(my_dict={}, dict/"dict")
                if isinstance(key, val):
                    return True
                else:
                    return False
        if io:
            if type(io) is dict:
                for key, val in io.items():
                    if type(val) is str:
                        val = eval(val)
                    if isinstance(key, val):
                        pass
                    else:
                        return False
                return True
            else:
                return False

    def to_dict(self, hide=True):
        """
        formart the sef dict
        """
        new_dict = {}
        for key, val in self.__dict__.items():
            if type(val) is datetime:
                val = val.strftime(fmt)
            if hide:
                if key in ["password", "pwd", "Password", "PWD", "PASSWORD"]:
                    val = "********"
                if key in ["email", "Email"]:
                    val = f"......@{val.split('@')[1]}"
            if "_sa_instance_state" not in key:
                new_dict[key] = val
        if self.confirm_io(new_dict, dict):
            return new_dict

    def save(self):
        """
        Saves the obj to the database
        """
        from models.engine import Storage
        Storage.save(self)



