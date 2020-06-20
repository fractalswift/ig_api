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


# Now use the id to get a list of index epics (flatten the list)

penultimate_row_of_tree_ids = [row["nodes"] for row in all_indices_ids]

flattened = [val for sublist in penultimate_row_of_tree_ids for val in sublist]


# Now create a list of epics from these ids

info = [get_id(row["id"]) for row in flattened]

# pprint.pprint(info)

almost_there = [row["markets"] for row in info]

flattened_finally = [val for sublist in almost_there for val in sublist]

epics = [row["epic"] for row in flattened_finally]

pprint.pprint(epics)
