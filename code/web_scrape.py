# Web scraping example

import requests
from bs4 import BeautifulSoup

url = "http://example.org"
req = requests.get(url)
cont = req.content
pcont = BeautifulSoup(cont, "html.parser")
print(pcont)