import requests
import re

URL = "https://cleantalk.org/blacklists/ivanov@gmail.com"

html = requests.get(URL).text

result = re.findall("[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+", html)

print(result)

