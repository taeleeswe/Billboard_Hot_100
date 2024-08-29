import requests
import pprint
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

Client_ID = os.environ["CLIENT_ID"]
Client_Secret = os.environ["CLIENT_SECRET"]

URL = "https://www.billboard.com/charts/hot-100/"

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")
respond = requests.get(URL + date)
soup = BeautifulSoup(respond.text, "html.parser")
song_titles_spans = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in song_titles_spans]

print(song_titles)

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                scope="playlist-modify-private",
                                                redirect_uri="http://example.com",
                                                client_id=Client_ID,
                                                client_secret=Client_Secret,
                                                show_dialog=True,
                                                cache_path="token.txt"
                                                ))

user_id = sp.current_user()["id"]
print(user_id)

# Searching spotity for songs
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # pprint.pp(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

# Adding songs into new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)