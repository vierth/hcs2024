import re

# if we want to match a number from 0 to 9
# \d
result = re.search(r'\d', 'It is the year 2024')
print(result)

# \D matches anything that is not a number
result = re.search(r'\D', 'It is the year 2024')
print(result)

# \s matches whitespace
result = re.search(r'\s', 'It is the year 2024')
print(result)

# if we want to match new lines: \n
# if we want to match tabs: \t

# \w matches letters or numbers
result = re.search(r'\w', 'It is the year 2024')
print(result)

# \@ matches NOT letters or numbers
result = re.search(r'\W', 'It is the year 2024')
print(result)

# . match everythign except a new line character
result = re.search(r'.', 'It is the year 2024')
print(result)

# \b matches a word boundary
result = re.search(r'\bship', "My spaceship is a ship")
print(result)

# a ? makes the match optional
result = re.search(r'humou?r', "humor")
print(result)

# + in conjunctino with something else, we will search for it one or more times
result = re.search(r"\d+", "It is the year 2024")
print(result)

# * will search zero or more times
result = re.search(r'humou*r', 'humouuuuuuuuuuuuuuur')
print(result)


