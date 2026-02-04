# Dictionaries - key-value pair; key ---> unique, unordered, immutable
data = {1:'Apple', 2:'Orange', 4:'Pineapple'}
# Accessing the dictionary
print(data[4]) # returns Pineapple that has key = 4
# data[3] - if key value doesnot exist ---> key error generated
print(data.get(2)) # returns values that has key 2
print(data.get(3)) # doesnot generate error and returns 'None'
print(data.get(1, "Lime")) # returns 'Apple' as value for key = 1, already exists
print(data.get(3, "Lime")) # returns 'Lime' as values doesnot exist by temporarily assigning  the value

# Other way to create dictionary
d = dict(name="Prachi", age=20, city="Mumbai")
print(d)
print(type(d))

# Adding the new value
d["email"] = "prachi@xyz.com"
print(d)

d["email"] = "new_prachi@xyz.com" # value gets overridden
print(d)

# Getting all keys from dictionary
for k in d.keys():
    print(k)

# Getting all values from dictionary
for v in d.values():
    print(v)

# Getting both keys and values from dictionary
for k, v in d.items():
    print(k, v)

# Removing elements
d.pop("age") # removes age key-value pair
print(d)
d.popitem() # removes last element pair
print(d)

# Merging two dictionaries ---> d1.update(d2)
d1 = {"name":"Max", "age":28, "email":"xyz@gmail.com"}
d2 = dict(name="Mary", age=27, city="Boston")
d1.update(d2)
print(d1)

# Dictionary using lists
keys = ['Apple', 'Orange', 'Pineapple', 'Grapes']
values = ['Red', 'Orange', 'Yellow', 'Green']
key_value = dict(zip(keys, values)) # merges two lists into dictionary
print(key_value)
key_value['Banana'] = 'Yellow' # adds data to dictionary
print(key_value)
del key_value['Banana'] # deletes specified key
print(key_value)

# List and dictionary inside another dictionary
program = {'JS':'Atom', 'C#':'VS', 'Python':['PyCharm', 'Spyder'], 'Java':{'JSE':'NetBeans', 'JEE':'Eclipse'}}
print(program)
# Accessing dictionary
print(program['JS']) # returns 'Atom'
print(program['Python']) # returns '['PyCharm', 'Spyder']'
print(program['Python'][1]) # returns 'Spyder'
print(program['Java']['JSE']) # returns 'NetBeans'

# modifying the copied dictionary using assignment operations, modifies original dictionary as well
# use cpy_d = d.cpoy() or cpy_d = dict(d) instead of cpy_d = d

# Dictionary Comprehension
cities = ['Mumbai', 'Paris', 'Dubai']
countries = ['India', 'France', 'UAE']

z = zip(cities, countries)
for i in z:
    print(i)

d_ = {city:country for city, country in zip(cities, countries)}
print(d_)
