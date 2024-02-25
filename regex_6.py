import re

# extract information
some_html = "<a href='www.yahoo.com'>"
some_more_html = "<div summary='www.google.com'>"

result = re.search(r'www\..+\.com', some_more_html)
print(result)


result = re.search(r"<a href='(.+)'>", some_html)
print(result.group(1))
print(result.groups())