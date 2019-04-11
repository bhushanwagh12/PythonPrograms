
import json

file = open("sample.json","r")
str_data = file.read()

json_data = json.loads(str_data)

print(json_data)
print(type(json_data))