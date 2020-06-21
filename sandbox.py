import pandas as pd
import numpy as np
import requests
import pprint
import json
import pprint
import matplotlib.pyplot as plt
from get_historical_data import get_hist_data

import os


mean_lookback = 10
divergence_lookback = 400


def sortSecond(val):
    return val[1]


def run_pairs_scan():

    pickles_to_read = os.listdir("pickles")

    hist_dfs = []
    for row in pickles_to_read:
        df = pd.read_pickle(f"pickles/{row}")
        epic = str(row)

        # add the name onto the df in a column...
        df["name"] = epic
        hist_dfs.append(df)

    coint_dfs = []
    for df in hist_dfs:

        x_df = df
        x_name = x_df["name"][0]

        for df in hist_dfs:

            y_name = df["name"][0]

            new_df = x_df.merge(df, on="time", how="inner")

            new_df = new_df[["time", "adj_close_x", "adj_close_y"]]

            name = f"{x_name}/{y_name}"

            row = [name, new_df]

            coint_dfs.append(row)

    diverged_pairs = []

    for row in coint_dfs:

        row[1]["ratio"] = row[1].adj_close_x / row[1].adj_close_y
        row[1]["sma"] = row[1].ratio.rolling(mean_lookback).mean()

        diverged_pairs.append(row)
    #     dist_pct = (abs(row[1]["ratio"] - row[1]["sma"]) / row[1]["sma"]) * 100

    #     max_dist = dist_pct[-divergence_lookback:-10].max()

    #     pct = (
    #         (row[1].ratio.iloc[-1] - row[1].sma.iloc[-1]) / row[1].sma.iloc[-1]
    #     ) * 100

    #     # if pct > max_dist * settings.divergence_percentile:

    #     #     if pct > settings.minimum_pct_divergence:

    #     diverged_pairs.append([row[0], pct])

    #     diverged_pairs.sort(key=sortSecond, reverse=True)

    return diverged_pairs


dfs = run_pairs_scan()

# pprint.pprint(dfs[3][0])
# df = dfs[3][1]
# pprint.pprint(df.tail())

for row in dfs:
    name = row[0]
    df = row[1]
    print(name)
    plt.plot(df.time, df.ratio)
    plt.plot(df.time, df.sma)
    plt.show()

