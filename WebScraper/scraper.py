import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Bsoup

my_url = 'https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709'
# openning and collecting the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# prasing to html
page_soup = Bsoup(page_html, "html.parser")

# grab each product
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "Scrape.csv"
f= open(filename,"w")
headers = "brand, product_name, Shipping \n"
f.write(headers)


# looping through the containers
for container in containers:
    brand=container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container= container.findAll("li", {"class": "price-ship"})
    shipping=shipping_container[0].text.strip()

    print("Brand: " + brand)
    print("Product Name: " + product_name)
    print("Shipping: " + shipping)

    f.write(brand  + "," +product_name.replace(",", "|") +"," +shipping +"\n" )
f.close()