import requests
import json
empid = 1
jsdata = {'empname': 'jassi', 'empage': 25}

headers = {'content-type': 'application/json'}
url = 'http://127.0.0.1:8000/api/'
resp = requests.put(url + str(empid)+"/", data=json.dumps(jsdata))
print(resp.json())