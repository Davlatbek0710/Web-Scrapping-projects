"""
    Automated Spotify playlist creation usign BeatifulSoup and Spotify WEB API docs
    First we fetch top 100 song in specified date format YYYY-MM-DD from user, 
    we scrape the data from https://www.billboard.com/charts/hot-100/    +    date   
    ex: https://www.billboard.com/charts/hot-100/  +  "2020-02-15"
    after fetching all 100 top song names we create a playlist usign spotipy module, after successful authontication.
    i.e:
        You need to have:
        - CLIENT_ID
        - CLIENT_SECRET
        you can get these 👆datas after creating an app in https://developer.spotify.com/
    then you would need to read https://spotipy.readthedocs.io/en/2.22.1/ 
    for getting all things done!

    @uthor: Davlatbek Kobiljonov
                                                                                            12/05/2024
"""




import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Get the desired date from the user
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/"

# Fetching data from Billboard website
result = requests.get(url + date)
soup = BeautifulSoup(result.text, "html.parser")

# Extracting song names from the Billboard chart
all_songs = soup.select(selector="div ul li.lrv-u-width-100p ul h3")
song_names = [x.getText().strip() for x in all_songs]

# Authentication with Spotify
CLIENT_ID = "fbf067d2fd56448ba05a7b1ed3da437e"
CLIENT_SECRET = "e2ba44252faf4be194501819bc29816d"
SPOTIPY_REDIRECT_URI = "http://example.com"

# Setting up Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    show_dialog=True,
    scope="playlist-modify-private",
    cache_path="token.txt"
))

# Fetching URIs of all songs from Spotify
year = date.split('-')[0]
song_uris = []

# Searching for each song and adding its URI to the list
for song in song_names:
    try:
        result = sp.search(q=f"track: {song} year: {year} limit: 5", type="track")
        artist_name = result['tracks']['items'][0]['album']['artists'][0]['name']
        link = result['tracks']['items'][0]['external_urls']['spotify']
        print(f"{song} - {artist_name}\n{link}")
        song_uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating playlist in Spotify and adding all 100 songs
user_id = sp.current_user()['id']

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
