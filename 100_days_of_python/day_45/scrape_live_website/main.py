import requests
from bs4 import BeautifulSoup
URL = "https://news.ycombinator.com/"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, 'html.parser')

article_titles = soup.select(".titlelink")
link_subtext = soup.select(".score")

for link in article_titles:
    print(link.get_text())
    print(link.get("href"))
    

upvotes = [int(score.get_text().split()[0]) for score in link_subtext]
print(upvotes)

print(upvotes.index(max(upvotes)))
