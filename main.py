import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

Client_ID = os.environ["CLIENT_ID"]
Client_Secret = os.environ["CLIENT_SECRET"]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=Client_ID,
                                                           client_secret=Client_Secret))

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

respond = requests.get(URL + date)


soup = BeautifulSoup(respond.text, "html.parser")
song_titles_spans = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in song_titles_spans]

print(song_titles)
