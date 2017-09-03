import sys

from spotify.data_collector import get_top_songs
from spotify.playlists import create_playlist
from config import USER
from spotify.spotify import get_authenticated_instance, SpotifyAuthException
from datetime import datetime

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def get_playlist_name():
    now = datetime.now()
    return "%s %s" % (months[now.month - 2], str(now.year))


def log(line, is_error=False):
    with open("log.txt", "a") as file:
        file.write("[" + str(datetime.now()) + "]: " + ("ERROR: " if is_error else "") + line + "\n")


try:
    spotify = get_authenticated_instance()
    log("Logged in successfully...")
except SpotifyAuthException:
    log("Failed to login to Spotify!", True)
    sys.exit(0)

top_songs = get_top_songs(spotify, 50, "short_term")
create_playlist(spotify, USER, get_playlist_name(), top_songs)

log("Successfully created a playlist with " + str(len(top_songs)) + " songs")
