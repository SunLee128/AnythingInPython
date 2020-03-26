from random import choice  # DON'T CHANGE!
person = {
    "first_name": "sun",
    "last_name": "lee",
    "is_funny": False,
    "age": 101,
    "gender": "Female"
}

# accessing Dictionary values
person["first_name"]  # "sun"
person["age"]  # 101

# iterating Dictionary values using .values()
for value in person.values():
    print(value)
# "sun"
# "lee"
# False
# 101
# "Female"

# accessing all keys in a Dictionary using .keys()
for key in person.keys():
    print(key)
# "first_name"
# "last_name"
# "is_funny"
# "age"
# "gender"

# accessing all keys and values using .items()
for key, value in person.items():
    print(key, value)
# first_name "sun"
# last_name "lee"
# is_funny False
# age 44
# gender "Female"

# Does a dictionary have a key?
"age" in person  # True
"awesome" in person  # False

# Does a dictionary have a value?
"sun" in person.values()  # True
"No" in person.values()  # False

#######################################################
food = choice(["cheese pizza", "quiche", "morning bun",
               "gummy bear", "tea cake"])  # DON'T CHANGE!

bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print("{} left".format(bakery_stock[food]))
else:
    print("We don't make that")
#######################################################

# clear - Clears all the keys and values in a dictionary:
d = dict(a=1, b=2, c=3)
d.clear()
d  # {}

# copy - Makes a copy of a dictionary
d = dict(a=1, b=2, c=3)
c = d.copy()
c  # {'a': 1, 'b': 2, 'c': 3}
c is d  # False

# fromkeys - creates key-value pairs from comma separated values:
{}.fromkeys("a", "b")  # {'a': 'b'}
{}.fromkeys(["email"], 'unknown')  # {'email': 'unknown'}
{}.fromkeys("a", [1, 2, 3, 4, 5])  # {'a': [1, 2, 3, 4, 5]}

#######################################################

game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo",
                   "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"]
initial_game_state = dict.fromkeys(game_properties, 0)
#######################################################


# get - Retrieves a key in an object and return None instead of a KeyError if the key does not exist:
d = dict(a=1, b=2, c=3)
d['a']  # 1
d.get('a')  # 1
d['b']  # 2
d.get('b')  # 2
d['no_key']  # KeyError
d.get('no_key')  # None

# pop - Takes a single argument corresponding to a key and removes that key-value pair from the dictionary. Returns the value corresponding to the key that was removed.
d = dict(a=1, b=2, c=3)
d.pop()  # TypeError: pop expected at least 1 arguments, got 0
d.pop('a')  # 1
d  # {'c': 3, 'b': 2}
d.pop('e')  # KeyError

# popitem - Removes a random key in a dictionary
d = dict(a=1, b=2, c=3, d=4, e=5)
d.popitem()  # ('d', 4)
d.popitem('a')  # TypeError: popitem() takes no arguments (1 given)

# update - Update keys and values in a dictionary with another set of key value pairs.
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}
second.update(first)
second  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# let's overwrite an existng key
second['a'] = "AMAZING"
# if we update again
second.update(first)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# the update overrides our values
second  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Dictionary comprehension
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)  # {'first': 1, 'second': 4, 'third': 9}

{num: num**2 for num in [1, 2, 3, 4, 5]}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)  # {'A': '1', 'B': '2', 'C': '3'}

# Dictionary comprehension with conditions
num_list = [1, 2, 3, 4]

{num: ("even" if num % 2 == 0 else "odd") for num in num_list}

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}


