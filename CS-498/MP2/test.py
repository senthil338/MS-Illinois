import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2"

payload = {
	"graphApi": "https://j0qvs8fr3l.execute-api.us-east-1.amazonaws.com/default/myfunc1",
	"botName": "myproj", 
	"botAlias": "myprojecbotalias",
	"identityPoolId": "us-east-1:6b86bc39-0341-4f3b-bef3-3fa0d4c3491a",
	"accountId": "092939318731",
	"submitterEmail": "786.senthil@gmail.com",
	"secret": "QCpCaJ7BJCxF4kiG",
	"region": "us-east-1"
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)