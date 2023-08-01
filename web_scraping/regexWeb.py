import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import datetime

def getLinks(articleURL):
    html = urlopen("https://en.wikipedia.org" + articleURL)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)