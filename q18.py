'''
18. Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python.
'''

import json

# help(json)
test_dict = {
  'name': 'Ayush',
  'age': 23
}
json_string = json.dumps(test_dict, indent=4)
print(type(json_string))
print(json_string)

result_dict = json.loads(json_string)
print(type(result_dict))
print(result_dict)