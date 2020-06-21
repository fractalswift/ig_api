import pandas as pd
import numpy as np
import requests
import pprint
import json
import matplotlib.pyplot as plt
from get_historical_data import get_hist_data


# get the list of current epics (don't forget to update them first
# # by tunning indices)
with open("current_epics.txt", "r") as f:
    epics = f.read().split("\n")

# Remove null values
epics = [row for row in epics if row]

startdate = "2020:06:10-10:00:00"
enddate = "2020:06:19-10:00:00"
resolution = "HOUR"
# epic = "IX.D.StoxxBank.MONTH2.IP"


# # Iterate through epics and get their historical data
# just top 10 for now
all_dfs = []
broken_epics = []
for epic in epics[:10]:
    try:
        df = get_hist_data(epic, resolution, startdate, enddate)
        all_dfs.append([epic, df])

    except Exception:
        broken_epics.append(epic)


# pickle them so I can experiment without making this call a million times
# remeber all_dfs is [epic, df] not just list of dfs
for row in all_dfs:

    row[1].to_pickle(f"pickles/{row[0]}")

# Tell me success vs failure
print(f"Success: {len(all_dfs)} Failure: {len(broken_epics)} ")

# simple_df = get_hist_data(epic, resolution, startdate, enddate)
# print(simple_df.tail())

# print one out just to see if it works
simple_df = all_dfs[0][1]
plt.plot(simple_df.time, simple_df.adj_close)
plt.show()
print(df.tail())

# pprint.pprint(prices["prices"][0:3])
