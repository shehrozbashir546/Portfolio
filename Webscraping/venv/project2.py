import bs4
import requests

base_URL = "http://quotes.toscrape.com/"
res = requests.get(base_URL)
soup = bs4.BeautifulSoup(res.text,"lxml")
#print(soup)

#       Create a set of all names of the authors on the first page.
author = soup.select(".author")
authorSet = set()
for name in author:
    authorSet.add(name.text)
#print(authorSet)

#       Create a list of all the quotes on the first page

quote_s = soup.select('.text')

QuoteList = []
for quote in quote_s:
    QuoteList.append(quote.text)

print(QuoteList)