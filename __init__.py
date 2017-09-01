from spotify import spotify
spotify = spotify.get_instance()

results = spotify.search(q="all time low")
for i, t in enumerate(results['tracks']['items']):
    print(' ', i, t['name'])