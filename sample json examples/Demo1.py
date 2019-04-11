
import json
data = {
    "employee": {
        "name": "Ravi",
        "company": "Sathya"
    }
}
file = open("sample.json","w")
json.dump(data,file)


