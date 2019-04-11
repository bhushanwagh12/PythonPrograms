
import json
import requests

response = requests.get("https://api.myjson.com/bins/74vt6")
print(response.text)

data = json.loads(response.text)
print(data)