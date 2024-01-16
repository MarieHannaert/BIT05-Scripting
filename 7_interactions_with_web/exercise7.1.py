#!/usr/bin/python3
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
url = "http://pfam.xfam.org/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
data_content = response.read()
soup = BeautifulSoup(data_content, 'html.parser')


# Print parse tree in better format
for link in soup.findAll('a'):
    if link.get('href') == "None":
        continue
    print(link.get('href'))
