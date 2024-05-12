"""
Dicionarios sao estruturas de tipo key e valor {'key': 'valor"}, key=indice
"""

people = {}

key = 'name'

people[key] = 'Luiz Otavio'
people['surname'] = 'Miranda'

print(people[key])

people[key] = 'Maria'
# del people['surname']
print(people)
print(people['name'])

if people.get('surname') is None: # return key's value
    print('Not Exist')
else:
    print(people['surname'])