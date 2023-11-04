#!/usr/bin/python3
"""
test all
"""
import sys, os

sys.path.append("..")

from models.base import BaseModel, Base
from models.user import User
from models.item import Item
from models.uitem import UItem
from models.tools.create import Create_Item
from models.ml.transformer import Transformer
from models.ml.analyzer import Analyzer
from models import *


# item = "mouse"
# # print(sys.argv)
# if len(sys.argv) > 1:
#     item = str(sys.argv[1]).replace(" ", "+")


# url = f"https://www.jumia.co.ke/catalog/?q={item}"
# create = Create_Item(url)
# create.new()

# tsf = Transformer()
# df = tsf.get_uitem_df()
# fig = tsf.get_price_over_time_fig(df)
anl = Analyzer()
# path = anl.get_price_over_time_fig(item="jikokoa xtra")
# path = anl.get_price_range(item="jikokoa xtra")
df = anl.get_df()
print(df.columns)



