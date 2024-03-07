# in order to access th einternet we must connect to it
import urllib.request

# put url in variable
url = "https://en.wikipedia.org/wiki/United_States_Attorney_for_the_Southern_District_of_New_York"

with urllib.request.urlopen(url) as request:
    contents = request.read()

print(contents)