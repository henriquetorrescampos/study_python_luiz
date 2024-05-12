"""
Useful methods for dictionaries
"""

people = {
    'name': 'Luiz Otavio',
    'surname': 'Miranda',
    'age': 25,
}

print(len(people)) # return quantity of keys
print(people.keys()) # return keys of dictionary
print(people.values()) # return values of dictionary keys
print(people.items()) # return key and value
print(people.setdefault()) # add value to a key doesn't exist



# for value in people.values():
#     print(value)

# for key, value in people.items():
#     print(key, value)

