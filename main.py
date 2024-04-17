import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
from creds import CLIENT_ID, CLIENT_SECRET, SCOPE, USERNAME,REDIRECT_URL

token=SpotifyOAuth(scope=SCOPE,username=USERNAME,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URL)
spotify=spotipy.Spotify(auth_manager=token)

def tracks(text):
    songs=list()
    for word in text.split(' '):
        songs.append(spotify.search(word,type="track")['tracks']['items'][0]['uri'])
    return songs

def make_playlist(text,name,desc):
    spotify.user_playlist_create(user=USERNAME,name=name,description=desc)
    playlist_id=spotify.user_playlists(user=USERNAME)['items'][0]['id']
    spotify.playlist_add_items(playlist_id=playlist_id,items=tracks(text))
    

print('welcome to textlist, pls gimme')
name=input('a name for your playlist: ')
desc=input('a description for your playlist: ')
text=input('personalized message: ')
print('creating playlist...')

make_playlist(text,name,desc)

print('thank you for using me, pls check ur profile have a gud day ')


