import requests
from bs4 import BeautifulSoup

url = "https://pypi.org/project/duckduckgo-search/"

webPages = requests.get(url)

screap = BeautifulSoup(webPages.content, "html.parser")
header = screap.find("h1").get_text()