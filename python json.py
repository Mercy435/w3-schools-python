'''JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation'''

import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
print()

# a Python object (dict):
x = {"name": "John","age": 30, "city": "New York"}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
print()

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''When you convert from Python to JSON, Python objects are converted
into the JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null'''

x= {"name": "John","age": 30, "married": True, "divorced": False, "children": ("Ann","Billy"), "pets": None,
  "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1} ]}
print(json.dumps(x))
print(json.dumps(x, indent=3))
print()
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print()
print(json.dumps(x, indent=4, sort_keys=True))