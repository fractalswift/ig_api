import pandas as pd
import numpy as np
import requests
import pprint
import json

from auth_session import headers, payload

with open("current_epics.txt", "r") as f:
    epics = f.read().split("\n")

# Remove null values
epics = [row for row in epics if row]

startdate = "2020:03:22-10:00:00"
enddate = "2020:04:22-10:00:00"
resolution = "HOUR"
epic = "CS.D.BITCOIN.TODAY.IP"

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


print(df.head())

# pprint.pprint(prices["prices"][0:3])
