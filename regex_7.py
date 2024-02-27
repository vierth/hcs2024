import re

some_html = "<p>This is some information like you see etc</p><p>some more information</p>"

results = re.finditer(r'<(.+?)>', some_html)

for r in results:
    print(r.group(1))

my_string = "arrrglebarrgle"

results = re.finditer(r'a.+?e',my_string)
for r in results:
    print(r)

# * and the + are greedy operators, trying to match the longest possible match