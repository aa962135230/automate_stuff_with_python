import json

python_value = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

string_of_json_data = json.dumps(python_value)
print(string_of_json_data)