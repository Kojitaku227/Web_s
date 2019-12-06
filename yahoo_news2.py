import requests
from bs4 import BeautifulSoup

# ニューストピックス
print("\nニューストピックス\n")

html = requests.get('https://news.yahoo.co.jp/topics/top-picks')

yahoo = BeautifulSoup(html.content, "html.parser")

# print(yahoo.select("li.topicsListItem"))

print("◆◇----------------------------")
for title in yahoo.select("div.newsFeed_item_title"):
    print(title.getText())
print("----------------------------◇◆")

# ニュースランキング
print("\n　　　　ニュースランキング\n")

html = requests.get('https://news.yahoo.co.jp/ranking/access/news')

ranking = BeautifulSoup(html.content, "html.parser")

print("◆◇----------------------------")

for title in ranking.select("div.newsFeed_item_title"):
    print(title.getText()[0:40])

print("----------------------------◇◆")
