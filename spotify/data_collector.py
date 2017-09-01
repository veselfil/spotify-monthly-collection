from spotify.spotify import get_authenticated_instance


def download_data(limit):
    spotify = get_authenticated_instance()
    return spotify.current_user_top_tracks(limit=limit, time_range='short_range')


def get_top_songs(limit):
    data = download_data(limit)
    data = [x['uri'] for x in data['items']]  # get the URIs of the songs
    return data
