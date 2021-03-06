
from bs4 import BeautifulSoup
import requests, json, lxml
def get_gse(query):
    headers = {
        'User-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
    }

    params = {
        'q': query,  # query
        'gl': 'us',  # country to search from
        'hl': 'en',  # language
    }

    html = requests.get("https://www.google.com/search", headers=headers, params=params)
    soup = BeautifulSoup(html.text, 'lxml')

    data = {'title':[],'link':[],'snippet':[]}
    #
    for result in soup.select('.tF2Cxc'):
        title = result.select_one('.DKV0Md').text
        link = result.select_one('.yuRUbf a')['href']

        # sometimes there's no description and we need to handle this exception
        try:
            snippet = result.select_one('#rso .lyLwlc').text
        except:
            snippet = None

        # data.append({
        #     'title': title,
        #     'link': link,
        #     'snippet': snippet,
        # })
        data['title'].append(title)
        data['link'].append(link)
        data['snippet'].append(snippet)

    # return (json.dumps(data, indent=2, ensure_ascii=False))
    return data
