def download_data(spotify, limit, time_range):
    return spotify.current_user_top_tracks(limit=limit, time_range=time_range)


def get_top_songs(spotify, limit, time_range):
    data = download_data(spotify, limit, time_range)
    data = [x['uri'] for x in data['items']]  # get the URIs of the songs
    return data
