import json
numbers = [2, 3, 5, 7, 11, 13]

slovar = {"name": "Ivan", "surname": "Ivanov"}

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(slovar, f)