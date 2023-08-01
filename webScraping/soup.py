from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("https://bit.ly/1Ge96Rw")
if title == None:
    print("Title could not be found")
else:
    print(title)
    html = urlopen("https://bit.ly/1Ge96Rw")
    bsObj = BeautifulSoup(html)
    nameList = bsObj.findAll(text="the prince")
    allText = bsObj.findAll(id="text")
    print(allText[0].get_text())