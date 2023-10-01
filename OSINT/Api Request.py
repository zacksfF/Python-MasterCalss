import requests
res = requests.get("https://api.github.com/search/users?q=javascript")
print(res.json())