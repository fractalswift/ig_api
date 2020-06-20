import requests
import json
import pprint

from settings import payload, headers

session_url = "https://api.ig.com/gateway/deal/session/"


# r = requests.post(url, data=json.dumps(payload), headers=headers)
session = requests.post(session_url, data=json.dumps(payload), headers=headers)

try:

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


def get_id(id):
    url = f"https://api.ig.com/gateway/deal/marketnavigation/{id}"
    res = requests.get(url, headers=headers)
    return json.loads(res.content)


pprint.pprint(get_id(130926550))
