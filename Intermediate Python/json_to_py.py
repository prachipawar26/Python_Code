# De-serialization / Decoding
import json

# use load() ---> get json data as file
# use load() ---> get json data as string

with open('person.json', 'r') as file:
    person = json.load(file) # loads(string) ---> other function

print(person)