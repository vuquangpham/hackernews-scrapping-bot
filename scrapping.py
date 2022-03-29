import requests
from bs4 import BeautifulSoup
from pprint import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titlelink')
votes = soup.select('.subtext>span:nth-child(1)')

def create_custom_hn(links, votes):
  hackernews_post = []
  for idx, item in enumerate(links):
    vote = votes[idx].getText()
    if ('hours' in vote):
      continue

    title = item.getText()
    href = item.get('href', None) #None is default params if not exist href
    vote = int(vote[:-7])
    if (vote > 100):
      hackernews_post.append({'title': title, 'vote': vote, 'href': href})
  return hackernews_post

hackernews_post = create_custom_hn(links, votes)
pprint(hackernews_post)