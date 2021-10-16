import bs4
import requests

#GOAL : Get a title of every book with a 2 star rating

base_URL = 'http://books.toscrape.com/catalogue/page-{}.html'
#res = requests.get(base_URL.format(1))
#soup = bs4.BeautifulSoup(res.text,"lxml")

#Every book is categorized by a class called Product Prod
#Prod = soup.select(".product_pod")

# Find the title
#FindTitle = example.select("a")[1]['title']
#print(FindTitle)

two_star_titles = []

for n in range(1,51):
    scrape_url = base_URL.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]["title"]
            two_star_titles.append(book_title)

print(f"The number of books with a two stars rating is {len(two_star_titles)} \n")

for n in range(0,195):
    print(two_star_titles[n])



