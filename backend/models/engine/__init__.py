#!/usr/bin/env python3
"""
init
"""
from models.engine.db_storage import DBStorage

Storage = DBStorage()
Storage.reload()
__all__ = ["Storage"]