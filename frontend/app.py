#!/usr/bin/python3
"""
This is the app.py file where the program starts exceting
"""
import sys
sys.path.append("/projects/Savy-Savvy/backend")
from models.item import Item
from models.uitem import UItem
from models.ml.transformer import Transformer
from models.ml.analyzer import Analyzer
from datetime import datetime

from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)

# CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", strict_slashes=False)
@app.route("/index", strict_slashes=False)
def home():
    """
    This is the home page for a Landing page
    """
    return render_template("index.html")

@app.route("/about", strict_slashes=False)
def about():
    """
    This is the official about page
    """
    return render_template("about.html")

@app.route("/display", strict_slashes=False)
def display():
    """
    This is the items display page
    """
    unique_items = []
    my_item = UItem()

    all_uitems = my_item.get_all_uitems(get_all=True)

    items = my_item.get_all_uitems()

    for item in items:
        item = str(item.type).replace("+", " ")
        if item not in unique_items:
            unique_items.append(item)
    now = datetime.now()
    return render_template("display.html", available_items=unique_items, items=items, time=now)

@app.route("/display/<item>", strict_slashes=False)
def display_item(item):
    """
    This will retuen the item details
    """
    it = Item()
    tsfm = Transformer()
    analyzer = Analyzer()
    items = []

    item = item.replace("+", " ")
    items = it.get_item(item)
    
    # print(items)
    # sam_df = tsfm.get_uitem_df()

    # item_df = sam_df[sam_df['type'] == item]
    # item_df.to_csv(f"{item.replace(' ', '_')}.csv")
    analyzer.get_all_times(item)

    path = analyzer.get_price_over_time_fig(item)
    img = f"..{str(path).split('frontend')[1]}"
    print(f"path: {path}\nimg: {img}")

    violin = analyzer.get_price_range(item)
    vln = f"..{str(violin).split('frontend')[1]}"
    now = datetime.now()

    # with open(f"static/analysis/item_summary.csv", "w") as f:
    #     f.write(sam_df.to_csv())

    return  render_template("display_item.html", items=items[0:15], time=now, fig_path=img, voilin=vln)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
