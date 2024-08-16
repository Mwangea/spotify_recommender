def format_track(track):
    return f"{track['name']} by {', '.join([artist['name'] for artist in track['artists']])}"