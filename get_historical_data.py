import pandas as pd
import numpy as np
import requests
import pprint
import json
import matplotlib.pyplot as plt

from auth_session import headers, payload


def get_hist_data(epic, resolution, startdate, enddate):

    prices_url = f"https://api.ig.com/gateway/deal/prices/{epic}/{resolution}?startdate={startdate}&enddate={enddate}"

    prices = json.loads(requests.get(prices_url, headers=headers).content)

    clean_prices = [
        [
            "time",
            "open_ask",
            "open_bid",
            "high_ask",
            "high_bid",
            "low_ask",
            "low_bid",
            "close_ask",
            "close_bid",
        ]
    ]

    for row in prices["prices"]:
        close_ask = row["closePrice"]["ask"]
        close_bid = row["closePrice"]["bid"]
        high_ask = row["highPrice"]["ask"]
        high_bid = row["highPrice"]["bid"]
        low_ask = row["lowPrice"]["ask"]
        low_bid = row["lowPrice"]["bid"]
        open_ask = row["openPrice"]["ask"]
        open_bid = row["openPrice"]["bid"]
        time = row["snapshotTime"]

        clean_prices.append(
            [
                time,
                open_ask,
                open_bid,
                high_ask,
                high_bid,
                low_ask,
                low_bid,
                close_ask,
                close_bid,
            ]
        )

    df = pd.DataFrame(clean_prices[1:], columns=clean_prices[0])

    df["adj_close"] = df["close_ask"] - round(abs(df["close_ask"] - df["close_bid"]))

    simple_df = df[["time", "adj_close"]]

    return simple_df
