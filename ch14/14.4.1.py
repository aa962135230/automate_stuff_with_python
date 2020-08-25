import json

string_of_jsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

json_data = json.loads(string_of_jsonData)
print(json_data)