import requests
import spotipy
from bs4 import BeautifulSoup
import spotify
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "5faff3deba1345abbf53fcb13f65ba53"
Client_Secret = "65c860fce4334c65b9072cf91b8ceb03"
scope = "playlist-modify-private"
redirect_uri = "http://example.com"
#user_id = "3126wdcwoo57ddtbj32hit4i6zxy"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID, client_secret=Client_Secret, scope=scope, redirect_uri=redirect_uri, cache_path="token.txt", show_dialog=False))
user_id = sp.current_user()["id"]
print(user_id)

date = input("What year would u like to travel? ")
website = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(website)
soup = BeautifulSoup(response.text, "html.parser")
song_tags = soup.select("li ul li h3")
songs = [tag.getText().strip() for tag in song_tags]
#
# for tag in song_tags:
#     songs.append(tag.getText)
# print(songs)

year = date.split("-")[0]
song_uri = []
for song in songs:
    result = sp.search(q=f"track:{song}, year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
