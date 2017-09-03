# from spotify import spotify
# spotify = spotify.get_authenticated_instance()
#
# results = spotify.current_user_top_tracks(limit=50, time_range='long_term')
# print (results)
# for i, t in enumerate(results['items']):
#     print(' ', i, t['name'], t['uri'])

from spotify.data_collector import get_top_songs
from spotify.playlists import create_playlist
from config import USER
from spotify.spotify import get_authenticated_instance
from datetime import datetime

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def get_playlist_name():
    now = datetime.now()
    return "%s %s" % (months[now.month - 1], str(now.year))


spotify = get_authenticated_instance()
top_songs = get_top_songs(spotify, 50, "short_term")
create_playlist(spotify, USER, get_playlist_name(), top_songs)
