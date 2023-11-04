#!/usr/bin/env python3
"""
ml test
"""

from models.ml.transformer import Transformer
from models.uitem import UItem
import os

tfm = Transformer()

# print(tfm.main_df.dtypes)

uitems = tfm.summarize_items(get_dicts=True)


# print("="*30)
# print(uitems[0])
ui = UItem(uitems[0])
# ui.save()

# for item in uitems:
#     ui = UItem(**item)
#     ui.save()

uis = ui.get_all_uitems(get_all=True)
print(len(uis))
# for it in uis:
#     print(it.to_dict())
#     print("="*50)

