#
# Script to scrape Reddit's '/r/DailyProgrammer' subreddit and extract the
# the 'Easy' challenges, along with the links to them
#

from __future__ import print_function
import re
from collections import defaultdict
import bs4
import requests
import pdb

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}

my_url = 'https://www.reddit.com/r/dailyprogrammer'
response = requests.get(my_url, headers=headers)

print("We got {} cookies: ", len(response.cookies))
for c in response.cookies:
    print("\t", c)

soup = bs4.BeautifulSoup(response.content, "lxml")
link_tags = soup.find_all('a', 'title')

categories = defaultdict(list)

for link in link_tags:
    # match = re.search("\[(.*?)\]")
    match = re.search("\[(\w+)\]", link.text)
    if match:
        category = match.group(1)
        categories[category].append(link)

for category in categories:
    links = categories[category]
    print(category)
    for link in links:
        print("\t", link.text, link.attrs['href'])
    if '[Easy]' in link.text:
        print(link.text, link.attrs['href'])

# print(response)
# pdb.set_trace()
