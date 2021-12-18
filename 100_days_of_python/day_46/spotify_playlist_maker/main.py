import requests
from bs4 import BeautifulSoup
from requests.models import HTTPError
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

week = input('Which year do you want to travel to?  Type the date in this format YYYY-MM-DD:')

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(url = f"{URL}{week}/").text

soup = BeautifulSoup(response, 'html.parser')

song_row = soup.find_all('h3', class_='a-font-primary-bold-s')
song_row = song_row[2:]
songs = [song.get_text().strip("\n") for song in song_row]

scope = "playlist-modify-private"
redirect_uri = "https://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,
                                                redirect_uri=redirect_uri))


YYYY = week.split('-')[0]
song_URI = []
for song in songs:
    

    try:
        results = sp.search(f"track:{song} year:{YYYY}", type='track', limit=1, market='US')
        result_URI = results['tracks']['items'][0]['uri']
        song_URI.append(result_URI)

    except IndexError:
        pass

new_playlist = sp.user_playlist_create(user='', 
                        name='python playlist',
                        public= False,
                        description='This is the playlist I created with python')
new_playlist_id = new_playlist['id']
sp.playlist_add_items(playlist_id=new_playlist_id, items=song_URI)
