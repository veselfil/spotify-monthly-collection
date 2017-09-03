def create_playlist(spotify, user, name, songs, public=True, thumbnail=None):
    """
    Creates a playlist.
    :param spotify: 
    :param name: 
    :param songs: 
    :param public: 
    :param thumbnail: 
    :return: 
    """
    if thumbnail is None:
        playlist_data = spotify.user_playlist_create(user, name, public)
        spotify.user_playlist_add_tracks(user, playlist_data["uri"], songs)
    else:
        raise Exception("Thumbnails are not yet supported.")
