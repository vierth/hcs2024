# in order to access th einternet we must connect to it
import urllib.request
import time

# save pages to fetch in list
sites = ["United_States_Attorney_for_the_Southern_District_of_New_York", "John_Holland_Group", "Keane_Gilford"]

for site in sites:
    # put url in variable
    url = "https://en.wikipedia.org/wiki/" + site

    with urllib.request.urlopen(url) as request:
        contents = request.read()

    html_string = contents.decode()

    with open(f'{site}.html', 'w', encoding='utf8') as wf:
        wf.write(html_string)
    
    time.sleep(.5)