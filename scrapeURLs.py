from bs4 import BeautifulSoup
import urllib.request

parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
url = "https://cloudinary.com/documentation/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True):
    print(link['href'])