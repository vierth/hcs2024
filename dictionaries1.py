# dictionaries in python are a nother very important datatype
# tend to be most useful when the order of the data does not matter

# creating an empty dictionry
my_dict = {}
my_dict = dict()

# create a dictionary with values
ages = {"Paul": 40, "Grop": 125}

# keys must be immutable
print(ages)

# access with keys
paul_age = ages["Paul"]
print(paul_age)

ages["Blboble"] = 25

print(ages)

# fetching non existant data gives you a key error
# ages["tom"]

# get the keys in a dictionary:
print(ages.keys())

for name in ages.keys():
    print(name)
    print(ages[name])

# just go through the values
for val in ages.values():
    print(val)

# let's get keys and values
for key, val in ages.items():
    print(key, val)