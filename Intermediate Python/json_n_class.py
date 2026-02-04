import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("Prachi", 20)

# Custom encoding function
def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True} # obj.__class__.__name__: True (returns class name)
    else:
        raise TypeError('Object of type User cannot be serialized into JSON')

userJSON1 = json.dumps(user, default=encode_user, indent=4)
print(userJSON1)

# JSONEncoder
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True} # obj.__class__.__name__: True (returns class name)
        return JSONEncoder.default(self, obj)
    
userJSON2 = json.dumps(user, cls=UserEncoder, indent=4)
print(userJSON2)

userJSON3 = UserEncoder(indent=4).encode(user)
print(userJSON3)

# Decoding
usr1 = json.loads(userJSON1)
print(usr1) # return dictionary format

# Custom decoding function
def decode_user(d):
    if User.__name__ in d:
        return User(name=d['name'], age=d['age'])
    return d

usr2 = json.loads(userJSON2, object_hook=decode_user)
print(usr2.name, usr2.age)

# JSONDecoder
from json import JSONDecoder
class UserDecoder(JSONDecoder):
    def decode(self, s):
        # 1. Convert the string to a regular dictionary first
        d = json.loads(s) 
        # 2. Check if it's a User (using your 'tag')
        if "User" in d:
            return User(d['name'], d['age'])
        return d

usr3 = UserDecoder().decode(userJSON3)
print(usr3.name, usr3.age)