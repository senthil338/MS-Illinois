import requests
import json
url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-test"
payload = {
        	"accountId": "009433843718",
		    "submitterEmail": "786.senthil@gmail.com",
		    "secret": "ZKPu4zcqCZ6JoCVk",
		    "ipaddress": "34.230.28.163"
    }
r = requests.post(url, data=json.dumps(payload))
print(r.status_code, r.reason)
print(r)