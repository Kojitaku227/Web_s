import requests
from bs4 import BeautifulSoup

html = requests.get('https://news.yahoo.co.jp')

yahoo = BeautifulSoup(html.content, "html.parser")

# print(yahoo.select("li.topicsListItem"))

print("◆◇----------------------------")
for title in yahoo.select("li.topicsListItem"):
    print(title.getText())
print("----------------------------◇◆")
