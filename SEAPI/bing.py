import requests
from bs4 import BeautifulSoup
import json
term = 'python'
url = 'https://www.bing.com/search?q={}&setlang=en-us'.format(term)
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')


data = []
[s.extract() for s in soup('span')]
unwantedTags = ['a', 'strong', 'cite']
for tag in unwantedTags:
    for match in soup.findAll(tag):
         match.replaceWithChildren()

results = soup.findAll('li', { "class" : "b_algo" })
for result in results:
    print("# TITLE: " + str(result.find('h2')).replace(" ", " ") + "\n#")
    print("# Link: " + str(result.find('div',{"class":"b_attribution"}).text).replace(" ", " ") + "\n#")

    print("# DESCRIPTION: " + str(result.find('p')).replace(" ", " "))

    print("# ___________________________________________________________\n#")
print(results)

#print(json.dumps(data, indent=2, ensure_ascii=False))