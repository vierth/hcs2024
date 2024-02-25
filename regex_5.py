import re

# match specific number of times
# {3}

result = re.search(r'a{3}', "will we match a or aaaaaaa")
print(result)

result = re.search(r'a{1,3}', "will we match a or aaaaaaa")
print(result)