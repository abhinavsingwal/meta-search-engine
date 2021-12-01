import requests
from bs4 import BeautifulSoup

query = "deep"
yahoo = "https://in.search.yahoo.com/search?q=" + query + "&n=" + str(10)
raw_page = requests.get(yahoo)

soup = BeautifulSoup(raw_page.text,'lxml')

for link in soup.select(".ac-algo.fz-l.ac-21th.lh-24"):
    print (link.text, link['href'])