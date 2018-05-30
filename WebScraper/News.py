import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Bsoup

url = 'https://bdnews24.com/technology/'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = Bsoup(page_html, "html.parser")

news = page_soup.find_all("div", {"class": "article news default "})

fname = "tech.csv"
f = open(fname, "w")
headers = "Heading , Summary \n"
f.write(headers)

for new in news:
    heading = new.div.a.text.strip()

    infos = new.find_all("div", {"class": "text"})
    info = infos[0].text.strip()
    print("News title: " + heading)
    print("Summary: " + info)

    f.write(heading + "," + info + "\n")

f.close()