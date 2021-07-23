import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
    
def getSoup(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup


def main():
    url = 'http://py4e-data.dr-chuck.net/known_by_Eden.html'
    for i in range(7):
        soup = getSoup(url)
        tags = soup('a')
        url = tags[17].get('href', None)
        
    print(tags[17].contents[0])

if __name__ == '__main__':
    main()