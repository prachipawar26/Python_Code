import json

person = {
    "name": "Prachi", "age": 20, "city": "Mumbai", "isEmployed": True, "titles": ["Engineer", "QA/Tester"]
}
print(person)

# use dump() ---> output json data as file
# use dumps() ---> output json data as string

personJSON1 = json.dumps(person)
print(personJSON1)

personJSON2 = json.dumps(person, indent=4)
print(personJSON2)

personJSON3 = json.dumps(person, indent=4, separators=(';', '=')) # seperators instead of , ---> ; and : ---> = (not recommended)
print(personJSON3)

personJSON4 = json.dumps(person, indent=4, sort_keys=True) # keys sorted alphabetically
print(personJSON4)

# Dumping into file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)