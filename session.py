import requests
import json
import pprint

from settings import payload, headers

session_url = "https://api.ig.com/gateway/deal/session/"


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

# market_url = "https://api.ig.com/gateway/deal/marketnavigation/93613"


# market_navigation = requests.get(market_url, headers=headers)

# pprint.pprint(json.loads(market_navigation.content))

startdate = "2020:03:22-10:00:00"
enddate = "2020:04:22-10:00:00"
resolution = "HOUR"
epic = "CS.D.BITCOIN.TODAY.IP"

prices_url = f"https://api.ig.com/gateway/deal/prices/{epic}/{resolution}?startdate={startdate}&enddate={enddate}"

prices = requests.get(prices_url, headers=headers)

pprint.pprint(json.loads(prices.content))
