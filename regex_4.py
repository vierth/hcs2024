import re

# let's talk about character sets

# a character set is formed with square brackets []
result = re.finditer(r'[abc]', 'can you run this restaurant')
for r in result:
    print(r)

result = re.search(r'lid[sz]', 'lidz')
print(result)

# match ranges
r'[a-e]'
r'[0-9]' # equivelant to \d
r'[a-zA-Z]'
r'[a-zA-Z0-9]' # equivelant to \w

# match not the character a
r'[^a]'

# match literal special characters
r'\.'
r'\+'
r'\\'

