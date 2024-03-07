# the requests library is very  useful for building api requests
import requests

api_url = "https://en.wikipedia.org/w/api.php"

headers = {"Content-Type":"application/json"}

search = {
    "action":"query",
    "format":"json",
    "titles":["Qing_dynasty"],
    "prop":"linkshere",
}

response = requests.post(api_url, params=search,headers=headers)

data = response.json()
print(data)