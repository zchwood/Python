import requests
from bs4 import BeautifulSoup
import csv

URL = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')

for lines in soup.find_all('p'):
    print(str(lines.getText()))