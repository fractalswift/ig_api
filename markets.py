import requests
import json
import pprint

from settings import payload, headers

session_url = "https://api.ig.com/gateway/deal/session/"


# r = requests.post(url, data=json.dumps(payload), headers=headers)
session = requests.post(session_url, data=json.dumps(payload), headers=headers)

try:

    cst = session.headers["CST"]

    pprint.pprint(session.headers["X-SECURITY-TOKEN"])

    x_security_token = session.headers["X-SECURITY-TOKEN"]


except Exception:
    print("there was a problem")


# Add the security token and client session token I just got
# into the headers array so now I can make authetnicated
# requests
headers["X-SECURITY-TOKEN"] = x_security_token
headers["CST"] = cst

# Now make a markets request!

market_url = "https://api.ig.com/gateway/deal/marketnavigation/"


market_navigation = requests.get(market_url, headers=headers)

# pprint.pprint(json.loads(market_navigation.content))

markets = json.loads(market_navigation.content)

# get the ids of all top level markets except shares
all_top_level = [row["id"] for row in markets["nodes"] if "Shares" not in "name"]

# print(all_top_level)


def get_id(id):
    url = f"https://api.ig.com/gateway/deal/marketnavigation/{id}"
    res = requests.get(url, headers=headers)
    return json.loads(res.content)


second_level = [get_id(row) for row in all_top_level]


print(f"There are {len(second_level)} rows in Second Level and here is the top one:")

pprint.pprint(second_level[0])


# Here is where the tree is not flat so we need some error handling
third_level = []

for row in second_level:
    try:
        third_level.append(get_id(row))
    except Exception:
        pass


print(f"There are {len(third_level)} rows in Third Level and here is the top one:")

pprint.pprint(third_level[0])


# pprint.pprint(get_id(second_level[0]))
