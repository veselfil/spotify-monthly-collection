from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from spotipy import oauth2 as oauth
from spotipy import Spotify


def get_instance():
    credentials = oauth.SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                 client_secret=SPOTIFY_CLIENT_SECRET)

    spotify = Spotify(client_credentials_manager=credentials)
    return spotify


def get_authenticated_instnace():
    credentials = oauth.SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                 client_secret=SPOTIFY_CLIENT_SECRET)
