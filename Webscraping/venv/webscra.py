import requests
import bs4

result = requests.get("http://example.com/")

soup = bs4.BeautifulSoup(result.text,"lxml")
title = soup.select('title')[0].get_text()
print(title)

para = soup.select('p')[0].get_text()
print(para)
print(type(para))