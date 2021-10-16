import bs4
import requests

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text,"lxml")

#Grabbing all the images
imgAll = soup.select('img')
#print(imgAll)
#Grab the first pic
img_1 = soup.select('img')[0]
#print(img_1)

#Grab the class of images in the article
imgClass = soup.select('.image')
#print(imgClass)

#Download the first image
print(img_1['src'])
imageLink = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')
imageLink.content
f = open('wikipediaImageGrab.jpg','wb')
f.write(imageLink.content)
f.close()
