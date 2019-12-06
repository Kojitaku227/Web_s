
import requests
from bs4 import BeautifulSoup
 
r = requests.get('https://finance.yahoo.co.jp/')
bs = BeautifulSoup(r.text, 'html.parser')
 
for i in bs.select("#one-header > dl"):
    print(i.getText())
for i in bs.select("#two-header > dl"):
    print(i.getText())
for i in bs.select("#three-header > dl"):
    print(i.getText())