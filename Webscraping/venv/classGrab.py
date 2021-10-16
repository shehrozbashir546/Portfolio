import bs4
import requests

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text,"lxml")
#Table of contents
TocText = soup.select('.toctext')
print(TocText)
#Grab one attribute
TocAttr = soup.select('.toctext')[0]
print(TocAttr)
