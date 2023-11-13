#!/usr/bin/python3
"""
Analyzer
"""
import seaborn as sbn
import numpy as np
import matplotlib.pyplot as plt
import json, os, sys
from .transformer import Transformer

sns = sbn

class Analyzer():
    """
    Analyzer class
    """
    tsfm = None
    df = None
    cwd = os.getcwd()
    root = f"{cwd.split('Save-Savvy')[0]}Save-Savvy"
    root_path = f"{root}/frontend/static/figures"

    def __init__(self, *args, **kwargs):
        """Init"""
        print(self.root_path)
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)

        self.tsfm = Transformer()
        df = self.tsfm.get_uitem_df()
        df = self.tsfm.clean_df_2(df)
        self.df = self.add_dates(df)

    def add_dates(self, df=df):
        """adds the dates periods"""
        try:
            df['year'] = df['updated_at'].dt.year
            df['month'] = df['updated_at'].dt.month
            df['day'] = df['updated_at'].dt.day
            df['hour'] = df['updated_at'].dt.hour
            df['minute'] = df['updated_at'].dt.minute
        except Exception as e:
            print(f"--A--(ALERT): {e}")
        return df

    def get_df(self):
        """
        returns the dataframe
        """
        return self.df

    def get_all_times(self, item):
        """
        Returns all the times
        """
        xs = ["year", "month", "day", "hour", "minute"]
        for x in xs:
            path = self.get_price_over_time_fig(item=item, x=x)


    def get_price_over_time_fig(self, item="all", x="updated_at", **kwargs):
        """
        Returns the figure of price over time
        xs = ["year", "month", "day", "hour", "minute"]
        """
        df = self.df
        if item == "all":
            df = self.df
        else:
            try:
                df = df[df['type'] == item]
            except Exception as e:
                print(f"--E--(ERR): {e}")
                pass

        rc={"font.size": 25, "xtick.labelsize": 14, "ytick.labelsize": 14}
        sns.set_style("darkgrid")
        sns.set(font_scale=1.2)
        # sns.set_palette("Set1")

        fig = plt.figure(figsize=(25, 10))
        figname = ""

        columns_to_plot = ['max_price', 'min_price', 'median_price', 'mean_price']

        for i, column in enumerate(columns_to_plot):
            linestyle = "-"
            if "mean" in column:
                linestyle = "dotted"
            sns.lineplot(data=df, x=x, y=column, label=column, marker="o", linestyle=linestyle, linewidth=4, markersize=8)
            line_color = sns.color_palette("Set1")[i]
            plt.setp(plt.gca().get_lines()[i], color=line_color)

        plt.xlabel('Date (updated_at)', fontsize=10)
        plt.ylabel('Price', fontsize=20)
        plt.title(f"Prices Over Time For {list(df['type'])[0]}", fontsize=20)
        plt.xticks(rotation=45)
        plt.tick_params(axis='both', which='major', labelsize=14)
        plt.legend(fontsize=20)

        mx = df["max_price"].max()
        lim = mx + (mx / 2)
        plt.ylim(0, lim)
        itm = str(list(df['type'])[0]).replace(" ", "_")
        path = f"{self.root_path}/price_over_time_fig_{itm}-{x}.png"
        plt.savefig(path)

        return path

    def get_price_range(self, item="all", **kwargs):
        """returns the path to then Voilin catplot for price range"""

        df = self.df
        if item == "all":
            pass
        else:
            try:
                df = df[df['type'] == item]
            except Exception as e:
                print(f"--E--(ERR): {e}")
                pass

        sns.set_style("darkgrid")
        price_columns = ['median_price', 'mean_price', 'min_price', 'max_price']

        g = sns.catplot(data=df.melt(id_vars='type', value_vars=price_columns),
                        x='type', y='value', hue='variable', kind='violin',
                        inner="quart", legend_out=False, height=10, aspect=2)

        g.fig.subplots_adjust(top=0.9)
        g.fig.suptitle('Violin Catplot for Prices by Item', fontsize=16)
        g.set_xlabels('Item')
        g.set_ylabels('Price')
        g.add_legend(title="Price Columns")

        itm = str(list(df['type'])[0]).replace(" ", "_")
        path = f"{self.root_path}/violin_price_range_{itm}.png"
        plt.savefig(path)

        return path
