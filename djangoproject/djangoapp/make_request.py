import requests
import json
empid = 10
jsdata = {'empname': 'jassi', 'empage': 25}

headers = {'content-type': 'application/json'}
url = 'http://127.0.0.1:8000/api/'
resp = requests.delete(url + str(empid)+"/",)
print(resp.json())
