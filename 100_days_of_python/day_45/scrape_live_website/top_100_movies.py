import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, 'html.parser')

movies = soup.find_all('h3', class_='title')
movies = [movie.get_text() for movie in movies]
movies = movies[::-1]

with open('movies_list.txt','a') as file:
    file = [file.write(f"{movie}\n") for movie in movies]