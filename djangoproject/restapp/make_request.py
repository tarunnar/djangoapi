import requests
import json
empid = 10,
jsdata = {
    "custid": 4,
    "custname": "trivedi",
    "custage": 27,
    "shopping": 80000
}
headers = {'content-type': 'application/json'}
url = 'http://127.0.0.1:8000/genericapi/3/'
resp = requests.delete(url)
print(resp.json())
