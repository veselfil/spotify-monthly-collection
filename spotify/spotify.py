from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SCOPES
from spotipy import oauth2 as oauth
from spotipy import Spotify
from spotipy import util


class SpotifyAuthException(Exception):
    def __init__(self, message):
        super().__init__(message)


def get_instance():
    credentials = oauth.SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                 client_secret=SPOTIFY_CLIENT_SECRET)

    spotify = Spotify(client_credentials_manager=credentials)
    return spotify


def get_authenticated_instance():
    token = util.prompt_for_user_token("vesel.fil",
                                       scope=SCOPES,
                                       client_id=SPOTIFY_CLIENT_ID,
                                       client_secret=SPOTIFY_CLIENT_SECRET,
                                       redirect_uri=SPOTIFY_REDIRECT_URI)

    if token:
        spotify = Spotify(auth=token)
        return spotify
    else:
        raise SpotifyAuthException("Failed to acquire Spotify auth token.")
