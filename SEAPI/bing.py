import requests
from bs4 import BeautifulSoup
import json
def bingsearch(term):

    url = 'https://www.bing.com/search?q={}&setlang=en-us'.format(term)
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {'title': [], 'link': [], 'snippet': []}

    [s.extract() for s in soup('span')]
    unwantedTags = ['a', 'strong', 'cite']
    for tag in unwantedTags:
        for match in soup.findAll(tag):
            match.replaceWithChildren()

    results = soup.findAll('li', {"class": "b_algo"})
    for result in results:
        # print("# TITLE: " + str(result.find('h2')).replace(" ", " ") + "\n#")
        # print("# Link: " + str(result.find('div', {"class": "b_attribution"}).text).replace(" ", " ") + "\n#")
        #
        # print("# DESCRIPTION: " + str(result.find('p')).replace(" ", " "))
        #
        # print("# ___________________________________________________________\n#")
        title = str(result.find('h2').text).replace(" ", " ")
        link = str(result.find('div', {"class": "b_attribution"}).text).replace(" ", " ")
        snippet = str(result.find('p').text).replace(" ", " ")
        # data.append({
        #     'title': title,
        #     'link': link,
        #     'snippet': snippet,
        # })
        data['title'].append(title)
        data['link'].append(link)
        data['snippet'].append(snippet)

    return data

#print(json.dumps(data, indent=2, ensure_ascii=False))