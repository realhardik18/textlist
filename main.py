import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from creds import CLIENT_ID, CLIENT_SECRET

def tracks(text):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID,client_secret=CLIENT_SECRET))
    songs=list()
    for word in text.split(' '):
        songs.append(spotify.search(word)['tracks']['items'][0])
    return songs


#print(len(tracks('hello there i am cool')))