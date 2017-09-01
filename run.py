# from spotify import spotify
# spotify = spotify.get_authenticated_instance()
#
# results = spotify.current_user_top_tracks(limit=50, time_range='long_term')
# print (results)
# for i, t in enumerate(results['items']):
#     print(' ', i, t['name'], t['uri'])

from spotify.data_collector import get_top_songs

top_songs = get_top_songs(50)