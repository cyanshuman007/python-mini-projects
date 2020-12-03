import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_story(hn_list):
    return sorted(hn_list, key= lambda k:k['votes'], reverse=True)

def create_custom(links, subtext):
    hn_list = []
    for inx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn_list.append({'title': title, 'link': href, 'votes': points})
    return sort_story(hn_list)

for item in create_custom(links, subtext):
    pprint.pprint(item)
