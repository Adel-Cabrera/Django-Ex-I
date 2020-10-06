# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

# JSON to Dictionary

import json

user_JSON = '{"first_name" : "Jhon", "age" : 30}'

user = json.loads(user_JSON)

print(user)
print(user['first_name'])
print(type(user))

# Dictionary to JSON (string)

car = {'maker' : 'Ford', 'model' : 'Mustang'}

car_JSON = json.dumps(car)
my_dict = car_JSON

print(car_JSON)
print(car_JSON)
