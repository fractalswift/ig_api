import requests
import json
import pprint

from settings import payload, headers

session_url = "https://api.ig.com/gateway/deal/session/"


# r = requests.post(url, data=json.dumps(payload), headers=headers)
session = requests.post(session_url, data=json.dumps(payload), headers=headers)

try:
    # pprint.pprint(json.loads(session.content))

    cst = session.headers["CST"]

    x_security_token = session.headers["X-SECURITY-TOKEN"]


except Exception:
    print("there was a problem")


# Add the security token and client session token I just got
# into the headers array so now I can make authetnicated
# requests
headers["X-SECURITY-TOKEN"] = x_security_token
headers["CST"] = cst

# Now make a markets request!


# ID of the node I am interested in, in this case, indices
# node_id = 93262 # This is the top indices level

# This is UK Indices
# node_id = 93333


def get_id(id):
    url = f"https://api.ig.com/gateway/deal/marketnavigation/{id}"
    res = requests.get(url, headers=headers)
    return json.loads(res.content)


indices_ids = [row["id"] for row in get_id(93262)["nodes"]]


all_indices_ids = [get_id(row) for row in indices_ids]

pprint.pprint(all_indices_ids)
