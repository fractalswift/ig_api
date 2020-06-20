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

