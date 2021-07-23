# WEB SCRAPING

# When a program or script pretends to be a browser and retrieves web pages,
# look at those webpages, extracts info, and then looks at more web pages

# WHY SCRAPE?

# Para acceder a datos que no se pueden acceder de otra forma, TENER CUIDADO PORQUE
# PODRIA SER ILEGAL

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

for tag in tags:
    print(tag.get('href', None))

spans = soup('span')

print(sum([int(span.contents[0]) for span in spans]))

