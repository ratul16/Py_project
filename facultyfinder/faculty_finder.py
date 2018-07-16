import requests as rq
from bs4 import BeautifulSoup as bs

def main():
	print("........Welcome to NSU faculty searcher........ \n")
	while (1):

		search = input("Enter your faculty name: ")

		url = "http://ece.northsouth.edu/people/type/faculty/"
		r = rq.get(url)
		soup = bs(r.content, "lxml")
		pages = []
		for buttons in soup.find_all("a", {"class": "page pagei"}):
			pages.append(url + buttons.get("href"))

		faculties = []

		for links in pages:
			r = rq.get(links)
			soup = bs(r.content, "lxml")
			for item in soup.find_all("tr"):
				for info in item.find_all("td", {"class":"faculty-name"}):
					faculties.append(info.text.strip())

		for item in faculties:
			if search in item:
				myitem = "\n".join(item.split(","))
				print("match Found!\n")
				print(myitem, "\n")
main()

